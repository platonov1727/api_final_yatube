from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    def validate(self, data):
        if self.context['request'].user != data.get('following'):
            return data
        raise serializers.ValidationError('Нельзя подписаться на себя')

    class Meta:
        fields = ('__all__')
        model = Follow
        validators = [
            UniqueTogetherValidator(queryset=Follow.objects.all(),
                                    fields=['user', 'following'],
                                    message='Повторная подписка запрещена')
        ]


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group

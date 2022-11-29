from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

MAX_LENGTH_OF_POST = 15


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название группы')
    description = models.CharField(max_length=128,
                                   verbose_name='Описание группы')
    slug = models.SlugField(max_length=50,
                            verbose_name='Адрес страницы группы',
                            help_text='Адрес страницы группы',
                            unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts')
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(Group,
                              on_delete=models.CASCADE,
                              related_name='posts',
                              blank=True,
                              null=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    text = models.TextField()
    created = models.DateTimeField('Дата добавления',
                                   auto_now_add=True,
                                   db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(User,
                             related_name='follower',
                             on_delete=models.CASCADE)
    following = models.ForeignKey(User,
                                  related_name='following',
                                  on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'],
                                    name='unique_follow')
        ]

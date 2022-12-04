from django.contrib import admin

from posts.models import Comment, Group, Post, Follow


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post_id', 'text', 'created')
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description', 'title', 'slug')
    list_filter = ('title', )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group', )
    search_fields = ('text', )
    list_filter = ('pub_date', )
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'following')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Follow, FollowAdmin)

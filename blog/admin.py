from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created',)
    fields = ['title', 'author', 'description']
    readonly_fields = ['created']


admin.site.register(Post, PostAdmin)

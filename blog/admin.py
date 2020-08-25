from django.contrib import admin

from .models import Post, Category, Link, Profile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'body',
                    'category', 'image', 'status']
    prepopulated_fields = {'slug': ('title',)}

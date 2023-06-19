# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import BookAuthor, Book


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bio')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'year',
        'author',
        'cover',
        'price',
        'is_special',
        'is_trending',
    )
    list_filter = ('author', 'is_special', 'is_trending')
    search_fields = ('slug',)

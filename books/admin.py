from django.contrib import admin
from books import models

@admin.register(models.BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'publication_year', 'available',)
    search_fields = ('author', 'title')
    list_filter = ('available',)

@admin.register(models.AuthorModels)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','nationality',)
    search_fields = ('name',)

from django.contrib import admin
from . models import Note, Category


class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'text', 'picture', 'created', 'category' )
    search_fields = ('user__username', 'title', 'created', 'text', 'category__cat_name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'cat_name')
    search_fields = ('user__username', 'cat_name')

admin.site.register(Note, NoteAdmin)
admin.site.register(Category, CategoryAdmin)


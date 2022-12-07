import django_filters
from . models import Category, Note


# https://django-filter.readthedocs.io/en/stable/ref/filterset.html

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            'cat_name':['icontains'],
        }

class NoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = ['category__cat_name', 'title']



from django import forms
from  .models import Note, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('cat_name',)

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('category', 'title', 'text', 'picture', )
        labels = {
            'category': 'Įrašo kategorija',
        }

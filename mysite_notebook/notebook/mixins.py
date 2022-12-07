from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Note

class CategoryNoteListMixin(MultipleObjectMixin):
	def get_context_data(self, *args, **kwargs):
		context = {}
		context['categories'] = Category.objects.all()
		context['notes'] = Note.objects.all()
		return context


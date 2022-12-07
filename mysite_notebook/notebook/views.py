from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView, MultipleObjectMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from django.db.models import Q

from . models import Note, Category
from . forms import NoteForm, CategoryForm
from . mixins import CategoryNoteListMixin
from . filters import CategoryFilter, NoteFilter


class CategoryNoteListView(LoginRequiredMixin, ListView, CategoryNoteListMixin):
    model = Category
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryNoteListView,self).get_context_data(*args, **kwargs)
        context['categories'] = context['categories'].filter(user=self.request.user).order_by('cat_name')
        context['notes'] = Note.objects.filter(user=self.request.user).order_by('-created')

        search_request = self.request.GET.get('search_input') or ''
        if search_request:
            context['notes'] = context['notes'].filter(Q(title__icontains=search_request)|Q(text__icontains=search_request))
        context['search_request'] = search_request

        return context


class NoteList(LoginRequiredMixin,ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    ordering = ['-created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = context['notes'].filter(user=self.request.user)

        search_request = self.request.GET.get('search_input') or ''
        if search_request:
            context['notes'] = context['notes'].filter(Q(title__icontains=search_request)|Q(text__icontains=search_request))
        context['search_request'] = search_request

        return context


class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note_detail'


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/upload_note.html'
    form_class = NoteForm
    success_url = reverse_lazy('category_note')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/update_note.html'
    success_url = reverse_lazy('category_note')


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note_delete.html'
    context_object_name = 'note'
    success_url = reverse_lazy('category_note')

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user)


# __________________________________________________________

class CategoryList(LoginRequiredMixin,ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = context['categories'].filter(user=self.request.user)
        return context


class CategoryDetail(LoginRequiredMixin, DetailView, MultipleObjectMixin):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category_detail'

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        object_list = Note.objects.filter(category_id=self.object)
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['notes'] = context['object_list']
        return context


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'category/upload_cat.html'
    form_class = CategoryForm
    success_url = reverse_lazy('upload_note')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoryCreate, self).form_valid(form)


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/update_cat.html'
    success_url = reverse_lazy('category_note')

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user)

class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category/cat_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category_note')

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user)

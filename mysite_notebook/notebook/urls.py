from django.urls import path
from . import views


urlpatterns = [
    path('home', views.CategoryNoteListView.as_view(), name='category_note'),


    path('notes', views.NoteList.as_view(), name='notes'),
    path('notes/<int:pk>', views.NoteDetail.as_view(), name='note_detail'),
    path('upload_note', views.NoteCreate.as_view(), name='upload_note'),
    path('update_note/<int:pk>', views.NoteUpdate.as_view(), name='update_note'),
    path('delete_note/<int:pk>', views.NoteDelete.as_view(), name='note_delete'),


    path('categories', views.CategoryList.as_view(), name='categories'),
    path('upload_category', views.CategoryCreate.as_view(), name='upload_cat'),
    path('update_category/<int:pk>', views.CategoryUpdate.as_view(), name='update_cat'),
    path('delete_category/<int:pk>', views.CategoryDelete.as_view(), name='cat_delete'),



]

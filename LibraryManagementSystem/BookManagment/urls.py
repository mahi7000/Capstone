from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_book),
    path('book_list/', views.book_list, name='book_list'),
    path('edit_book/', views.book_list, name='edit_book'),
    #path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('add_book/', views.add_book, name='add_book'),
    #path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('delete_book/', views.book_list, name='delete_book'),
]
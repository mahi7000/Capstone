from django.urls import path
from . import views

urlpatterns = [
    path('borrow_book/<int:book_id>/', views.borrow_book, name='borrow_book'),
]
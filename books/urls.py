from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_book, name='create_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('all/', views.get_all_books, name='get_all_books'), 
]

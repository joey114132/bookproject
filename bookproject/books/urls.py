from django.urls import path
from . import views
app_name = 'books'
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]

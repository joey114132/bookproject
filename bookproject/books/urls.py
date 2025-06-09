from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("add/", views.BookCreateView.as_view(), name="book_add"),
    path("<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("<int:pk>/edit/", views.BookUpdateView.as_view(), name="book_edit"),
    path("<int:pk>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
    path("<int:pk>/vote/", views.vote, name="vote"),
    path("<int:pk>/results/", views.BookResultsView.as_view(), name="results"),
]
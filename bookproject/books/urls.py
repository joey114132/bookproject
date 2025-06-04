from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.BookListView.as_view(), name="list"),
    path("<int:pk>/", views.BookDetailView.as_view(), name="detail"),
    path("<int:pk>/vote/", views.vote, name="vote"),
    path("<int:pk>/results/", views.BookResultsView.as_view(), name="results"),
]
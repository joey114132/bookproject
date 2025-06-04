from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book
from django.db.models import F

class BookListView(generic.ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"

class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

def vote(request, pk):
    book = get_object_or_404(Book, pk=pk)
    try:
        book.votes = F("votes") + 1
        book.save()
        return HttpResponseRedirect(reverse("books:results", args=(book.id,)))
    except Exception:
        return render(
            request,
            "books/book_detail.html",
            {
                "book": book,
                "error_message": "⚠️ 투표 처리 중 문제가 발생했습니다.",
            },
        )

class BookResultsView(generic.DetailView):
    model = Book
    template_name = "books/book_results.html"
    context_object_name = "book"
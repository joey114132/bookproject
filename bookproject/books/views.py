from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Book
from django.db.models import F

# 책 목록 보기
class BookListView(generic.ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"

# 책 상세 보기
class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

# 책 생성 (Create)
class BookCreateView(generic.CreateView):
    model = Book
    fields = ["title", "author"]
    template_name = "books/book_form.html"
    success_url = reverse_lazy("books:book_list")

# 책 수정 (Update)
class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ["title", "author"]
    template_name = "books/book_form.html"
    success_url = reverse_lazy("books:book_list")

# 책 삭제 (Delete)
class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy("books:book_list")

# 투표 처리
def vote(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.votes = F("votes") + 1
        book.save()
        return HttpResponseRedirect(reverse("books:results", args=(book.id,)))
    return render(request, "books/book_detail.html", {
        "book": book,
        "error_message": "Invalid access.",
    })

# 결과 보기
class BookResultsView(generic.DetailView):
    model = Book
    template_name = "books/book_results.html"
    context_object_name = "book"
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
def book_list(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:book_list')
    else:
        form = BookForm()
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'form': form, 'books': books})
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('books:book_list')

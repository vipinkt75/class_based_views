from django.shortcuts import render
from . models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'hello': "enthan bro modayaano",
        "book": books
    }
    return render(request, 'web/index.html', context)

def detail(request, slug):
    book = Book.objects.get(slug=slug)
    context = {
        "book": book
    }
    return render(request, 'web/shopdatial.html', context)

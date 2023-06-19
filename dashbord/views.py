from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from web.models import Book
from django.contrib.auth.mixins import LoginRequiredMixin


def navbar(request):
    return render(request, 'web/navbar.html')


def index(request):
    return render(request, 'web/index.html')


def buttons(request):
    return render(request, 'web/buttons.html')


def login(request):
    return render(request, 'web/login.html')



class Index(TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = "hello"
        return context
    

class BookListView(ListView):
    template_name = "dashboard/books.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.filter()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = f"Hello {self.request.user}"
        return context
    

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    



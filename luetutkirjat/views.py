from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models

class BookListView(ListView):
    model = models.Book

class BookDetailView(DetailView):
    model = models.Book

class BookCreateView(CreateView):
    model = models.Book
    fields ='__all__'
    success_url = "/book/"

class BookUpdateView(UpdateView):
    model = models.Book
    fields ='__all__'
    success_url = "/book/"

class BookDeleteView(DeleteView):
    model = models.Book
    fields ='__all__'
    success_url = "/book/"
    

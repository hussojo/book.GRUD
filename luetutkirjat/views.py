from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

class BookListView(ListView):
    model = models.Book

class BookDetailView(LoginRequiredMixin, DetailView):
    model = models.Book

class BookCreateView(LoginRequiredMixin, CreateView):
    model = models.Book
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    fields ='__all__'
    success_url = "/book/"

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Book
    fields ='__all__'
    success_url = "/book/"

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Book
    fields ='__all__'
    success_url = "/book/"
    

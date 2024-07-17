from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from . models import Book

# Create your views here.

class HomeViewPage(TemplateView):
    template_name = 'Home.html'

class BookListViewPage(ListView):
    model=Book
    template_name = 'BookList.html'
    context_object_name="Books"


class BookDetailsViewPage(DetailView):
    model=Book
    template_name = 'BookDetails.html'

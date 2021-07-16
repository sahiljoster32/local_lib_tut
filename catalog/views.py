from django.http import request
from django.shortcuts import render
from django.template import context
from .models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):
    """View function for home page of site."""

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_geners = Genre.objects.all().count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_geners': num_geners,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


def AuthorListView(request):
    author_objects = Author.objects.all()
    context = {
        "Author_list": author_objects,
    }
    return render(request, "Author_list.html", context=context)


def AuthordetailView(request, pk=0):
    author_object = Author.objects.get(pk=pk)
    author_name = author_object.__str__()
    author_dob = author_object.date_of_birth
    book_objects = Book.objects.filter(author=pk)
    context = {
        "author_name": author_name,
        "author_dob": author_dob,
        "book_lists": book_objects,
    }
    return render(request, "author_detail.html", context=context)


class BookDetailView(generic.DetailView):
    model = Book

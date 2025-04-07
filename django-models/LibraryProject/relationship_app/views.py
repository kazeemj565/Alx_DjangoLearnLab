# relationship_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

# Function-based view to list all books.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details.
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the new user.
            return redirect('list_books')  # Redirect to a view of your choice.
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# relationship_app/views.py
import logging
from django.shortcuts import render, get_object_or_404, redirect
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from .models import UserProfile
from .forms import BookForm  # Assume you have a form


logger = logging.getLogger(__name__)

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


def role_required(required_role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                if user_profile.role == required_role:
                    return view_func(request, *args, **kwargs)
            except UserProfile.DoesNotExist:
                logger.warning(f"UserProfile not found for user: {request.user.username}")
            return render(request, 'relationship_app/unauthorized.html')
        return login_required(_wrapped_view)
    return decorator

@user_passes_test(role_required('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(role_required('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(role_required('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Assume this exists
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})


@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'relationship_app/edit_book.html', {'form': form})


@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})


@permission_required('relationship_app.can_view_book')
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})




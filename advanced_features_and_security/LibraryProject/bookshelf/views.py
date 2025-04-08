
# Create your views here.
# bookshelf/views.py
import logging
from django.shortcuts import render, get_object_or_404, redirect
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from .models import UserProfile
from .forms import BookForm, ExampleForm  # Assume you have a form


logger = logging.getLogger(__name__)

# Function-based view to list all books.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

# Class-based view for library details.
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'bookshelf/library_detail.html'
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
    return render(request, 'bookshelf/register.html', {'form': form})


def role_required(required_role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                if user_profile.role == required_role:
                    return view_func(request, *args, **kwargs)
            except UserProfile.DoesNotExist:
                logger.warning(f"UserProfile not found for user: {request.user.username}")
            return render(request, 'bookshelf/unauthorized.html')
        return login_required(_wrapped_view)
    return decorator

@user_passes_test(role_required('Admin'))
def admin_view(request):
    return render(request, 'bookshelf/admin_view.html')

@user_passes_test(role_required('Librarian'))
def librarian_view(request):
    return render(request, 'bookshelf/librarian_view.html')

@user_passes_test(role_required('Member'))
def member_view(request):
    return render(request, 'bookshelf/member_view.html')


@csrf_protect
@permission_required('bookshelf.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Assume this exists
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})

@csrf_protect
@permission_required('bookshelf.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'bookshelf/edit_book.html', {'form': form})

@csrf_protect
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

@csrf_protect
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def search_books(request):
    query = request.GET.get("q", "")
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books})


def example_form_view(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        # process form.cleaned_data here
        pass
    return render(request, 'bookshelf/form_example.html', {'form': form})

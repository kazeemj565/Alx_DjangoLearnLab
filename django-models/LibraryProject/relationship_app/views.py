# relationship_app/views.py
import logging
from django.shortcuts import render, get_object_or_404, redirect
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.decorators import user_passes_test, login_required
from .models import UserProfile


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

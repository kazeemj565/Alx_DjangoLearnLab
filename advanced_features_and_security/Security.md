# Django Security Measures

## Project: LibraryProject

### 🔐 Security Settings
- `DEBUG = False` in production
- `SECURE_BROWSER_XSS_FILTER = True`
- `X_FRAME_OPTIONS = 'DENY'`
- `SECURE_CONTENT_TYPE_NOSNIFF = True`
- Cookies secured: `CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`
- `SECURE_HSTS_SECONDS = 31536000`
- `django-csp` enabled for content security policy

### 🧰 Forms & Templates
- All forms use `{% csrf_token %}` to protect against CSRF attacks

### 🔎 Views
- User input validated with Django forms
- Queries use Django ORM to avoid SQL injection
- Permissions enforced using `@permission_required(..., raise_exception=True)`

### 📦 Packages
- [`django-csp`](https://github.com/mozilla/django-csp) to manage CSP headers

---

Let me know if you want me to generate:
- Your `models.py` with custom permissions (`can_create`, `can_edit`, etc.)
- Updated `book_list.html` with permission-based UI display
- Testing instructions?

Or want help deploying this securely online (e.g., with Gunicorn, Nginx, HTTPS)?

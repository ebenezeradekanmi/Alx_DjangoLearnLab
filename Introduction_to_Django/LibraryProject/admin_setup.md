# Django Admin Integration for Book Model

## Objective
Configured the Django admin interface to manage the Book model for efficient data administration.

## Steps Implemented
1. Registered the Book model in `bookshelf/admin.py`.
2. Customized the admin interface with:
   - `list_display` for title, author, and publication_year.
   - `list_filter` for author and publication_year.
   - `search_fields` for title and author.
3. Created a Django superuser using `python manage.py createsuperuser`.
4. Accessed the admin panel at `http://127.0.0.1:8000/admin/` to verify CRUD operations.

## Code Example
```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

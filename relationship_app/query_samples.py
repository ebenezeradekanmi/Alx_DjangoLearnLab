import sys
import os

# --------------------------
# Ensure Python can find the Django project
# --------------------------
# Add the project root (folder containing manage.py) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

import django
django.setup()

# --------------------------
# Import models
# --------------------------
from relationship_app.models import Author, Book, Library, Librarian

# --------------------------
# Create sample data (if not exists)
# --------------------------
def create_sample_data():
    if not Author.objects.exists():
        # Authors
        a1 = Author.objects.create(name="Chinua Achebe")
        a2 = Author.objects.create(name="Wole Soyinka")

        # Books
        b1 = Book.objects.create(title="Things Fall Apart", author=a1)
        b2 = Book.objects.create(title="No Longer at Ease", author=a1)
        b3 = Book.objects.create(title="Ake", author=a2)

        # Library
        lib = Library.objects.create(name="Central Library")
        lib.books.add(b1, b2, b3)

        # Librarian
        Librarian.objects.create(name="Jane Doe", library=lib)

# --------------------------
# Query functions
# --------------------------
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    print(f"\nBooks by {author.name}:")
    for book in author.books.all():
        print(f"- {book.title}")

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in {library.name}:")
    for book in library.books.all():
        print(f"- {book.title}")

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    print(f"\nThe librarian for {library.name} is {library.librarian.name}")

# --------------------------
# Main
# --------------------------
if __name__ == "__main__":
    create_sample_data()
    get_books_by_author("Chinua Achebe")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")


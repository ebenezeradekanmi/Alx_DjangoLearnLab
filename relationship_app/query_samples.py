# relationship_app/query_samples.py
import os
import sys
import django

# Ensure the project root is in Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Setup Django
django.setup()

# Import your models
from relationship_app.models import Author, Book, Library, Librarian

# -------------------------
# Sample data creation
# -------------------------
def create_sample_data():
    if not Author.objects.exists():
        # Create Authors
        a1 = Author.objects.create(name="Chinua Achebe")
        a2 = Author.objects.create(name="Wole Soyinka")

        # Create Books
        b1 = Book.objects.create(title="Things Fall Apart", author=a1)
        b2 = Book.objects.create(title="No Longer at Ease", author=a1)
        b3 = Book.objects.create(title="Ake", author=a2)

        # Create Library
        lib = Library.objects.create(name="Central Library")
        lib.books.add(b1, b2, b3)

        # Create Librarian
        Librarian.objects.create(name="Jane Doe", library=lib)

# -------------------------
# Queries
# -------------------------
def get_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    print(f"Books by {author_name}: {[b.title for b in books]}")

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library_name}: {[b.title for b in books]}")

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    print(f"Librarian for {library_name}: {library.librarian.name}")

# -------------------------
# Run the script
# -------------------------
if __name__ == "__main__":
    create_sample_data()
    get_books_by_author("Chinua Achebe")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")

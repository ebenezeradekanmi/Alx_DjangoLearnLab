\# Create Operation



```python

from bookshelf.models import Book



\# Create a Book instance

book = Book.objects.create(title="1984", author="George Orwell", publication\_year=1949)

book

\# Output: <Book: 1984>




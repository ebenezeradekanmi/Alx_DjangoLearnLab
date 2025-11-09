# Retrieve Book instance(s)

```python
from bookshelf.models import Book

books = Book.objects.all()
books
# Expected Output: <QuerySet [<Book: 1984>]>
```

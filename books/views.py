from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Book

@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            author = data.get('author')
            published_date = data.get('published_date', None)

            if not title or not author:
                return JsonResponse({'error': 'Title and author are required.'}, status=400)

            book = Book.objects.create(
                title=title,
                author=author,
                published_date=published_date
            )
            return JsonResponse({'message': 'Book created successfully!', 'book_id': book.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON payload.'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method.'}, status=405)

@csrf_exempt
def delete_book(request, book_id):
    if request.method == 'DELETE':
        try:
            book = Book.objects.get(id=book_id)
            book.delete()
            return JsonResponse({'message': 'Book deleted successfully!'}, status=200)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found.'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method.'}, status=405)


def get_all_books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        books_data = [
            {
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'published_date': book.published_date.strftime('%Y-%m-%d') if book.published_date else None
            }
            for book in books
        ]
        return JsonResponse({'books': books_data}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method.'}, status=405)
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from .models import Book
import json

# Tag for the 'Books' section in Swagger
BOOKS_TAG = ['Books']

@swagger_auto_schema(
    method='post',
    operation_description="Create a new book",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the book'),
            'author': openapi.Schema(type=openapi.TYPE_STRING, description='Author of the book'),
            'published_date': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Publication date (YYYY-MM-DD)'),
        },
        required=['title', 'author'],
    ),
    responses={
        201: openapi.Response('Book created successfully!'),
        400: openapi.Response('Invalid input'),
    },
    tags=BOOKS_TAG  # Adding the 'Books' tag
)
@api_view(['POST'])
def create_book(request):
    try:
        data = request.data  # DRF automatically parses the body for us
        title = data.get('title')
        author = data.get('author')
        published_date = data.get('published_date', None)

        if not title or not author:
            return Response({'error': 'Title and author are required.'}, status=400)

        book = Book.objects.create(
            title=title,
            author=author,
            published_date=published_date
        )
        return Response({'message': 'Book created successfully!', 'book_id': book.id}, status=201)
    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON payload.'}, status=400)

@swagger_auto_schema(
    method='delete',
    operation_description="Delete a book by ID",
    responses={
        200: openapi.Response('Book deleted successfully!'),
        404: openapi.Response('Book not found'),
    },
    tags=BOOKS_TAG  # Adding the 'Books' tag
)
@api_view(['DELETE'])
def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return Response({'message': 'Book deleted successfully!'}, status=200)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found.'}, status=404)

@swagger_auto_schema(
    method='get',
    operation_description="Get all books",
    responses={
        200: openapi.Response(
            description="List of books",
            examples={
                'application/json': {
                    'books': [
                        {
                            'id': 1,
                            'title': 'The Great Gatsby',
                            'author': 'F. Scott Fitzgerald',
                            'published_date': '1925-04-10'
                        },
                        {
                            'id': 2,
                            'title': 'To Kill a Mockingbird',
                            'author': 'Harper Lee',
                            'published_date': '1960-07-11'
                        }
                    ]
                }
            }
        ),
        400: openapi.Response('Invalid request'),
    },
    tags=BOOKS_TAG  # Adding the 'Books' tag
)
@api_view(['GET'])
def get_all_books(request):
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
    return Response({'books': books_data}, status=200)

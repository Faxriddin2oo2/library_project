from .models import Book
from .serializers import BookSerializer

from rest_framework import generics


class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
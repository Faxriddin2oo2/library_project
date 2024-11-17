from django.template.context_processors import request
from django.urls import path

from .serializers import BookSerializer
from .views import BookListApiView, book_list_view, BookDetailApiView, BookUpdateApiView, BookDeleteApiView

urlpatterns = [
    path('', BookListApiView.as_view(),),
    path('<int:pk>/', BookDetailApiView.as_view()),
    path('<int:pk>/update', BookUpdateApiView.as_view()),
    path('<int:pk>/delete', BookDeleteApiView.as_view()),
    path('books/', book_list_view,)
]
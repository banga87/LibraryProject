# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, LibrarianViewSet, BookViewSet, BorrowingViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'librarians', LibrarianViewSet, basename='librarian')
router.register(r'books', BookViewSet, basename='book')
router.register(r'borrowings', BorrowingViewSet, basename='borrowing')

urlpatterns = [
    path('', include(router.urls)),
]

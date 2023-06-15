# views.py
from rest_framework import viewsets
from .models import Student, Librarian, Book, Borrowing
from .serializers import StudentSerializer, LibrarianSerializer, BookSerializer, BorrowingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.db.models import Q


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class LibrarianViewSet(viewsets.ModelViewSet):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # WHEN SEARCHING FOR A BOOK
    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search')

        if search_term:
            queryset = queryset.filter(Q(title__icontains=search_term) | 
                                       Q(author__icontains=search_term) |
                                       Q(genre__icontains=search_term))
        return queryset

    # WHEN BORROWING A BOOK...
    @action(detail=True, methods=['post'])
    def borrow(self, request, pk=None):
        book = self.get_object()
        student_id = request.data.get('student_id')

        # CHECK IF USER IS STUDENT
        if not student_id or not Student.objects.filter(id=student_id).exists():
            return Response({"error": "Student ID is required and should be valid."}, status=status.HTTP_400_BAD_REQUEST)
        
        # CHECK IF THE BOOK IS CURRENTLY BORROWED
        if book.is_borrowed:
            return Response({"error": "Book is already borrowed."}, status=status.HTTP_400_BAD_REQUEST)
        
        # CREATE BORROWING RECORD AND SAVE
        student = Student.objects.get(id=student_id)
        Borrowing.objects.create(student=student, book=book)
        book.is_borrowed = True
        book.save()
        
        return Response({"success": "Book borrowed successfully."})

    # WHEN RETURNING A BOOK...
    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        book = self.get_object()

        # CHECK IF BOOK IS BORROWED
        if not book.is_borrowed:
            return Response({"error": "Book is not borrowed."}, status=status.HTTP_400_BAD_REQUEST)
        
        # EDIT BORROWING RECORD TO REFLECT THE RETURN DATE
        borrow_record = Borrowing.objects.filter(book=book).latest('borrowed_date')
        borrow_record.return_date = timezone.now()

        # EDIT BOOK RECORD TO REFLECT THE RETURNED STATUS
        borrow_record.save()
        book.is_borrowed = False
        book.save()

        return Response({"success": "Book returned successfully."})


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

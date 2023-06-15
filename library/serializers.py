from rest_framework import serializers
from .models import Student, Librarian, Book, Borrowing

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
      model = Book
      fields = '__all__'


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = '__all__'
from rest_framework import serializers
from .models import Student, Librarian, Book, Borrowing

class BookSerializer(serializers.ModelSerializer):
    class Meta:
      model = Book
      fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    borrowed_books = models.ManyToManyField('Book', through='Borrowing', related_name='borrowed_books')


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    is_borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Borrowing(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(default=timezone.now() + timedelta(days=14))

    def __str__(self):
        return f"{self.student.user.username} borrowed {self.book.title}"
    
    """Overriding save() to solve the issue that default value for 'return_date' is calculated
    at time of server start. All 'Borrowings' would have the same 'return_date' if server
    runs for more than a day."""
    def save(self, *args, **kwargs):
        if not self.id:
            self.return_date = timezone.now() + timedelta(days=14)
        super().save(*args, **kwargs)
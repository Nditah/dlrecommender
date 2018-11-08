from django.db import models
from djangoratings.fields import RatingField

class Student(models.Model):
    regno = models.CharField(max_length=200, unique=True)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)

    def __str__(self):
        return self.regno

    class Meta:
        ordering = ('regno',)


class Material(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    subcategory = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Rating(models.Model):
     CHOICES = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 0),
    ) # list(zip(range(0, 6), range(0, 6)))
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rated = models.IntegerField(choices=CHOICES, default=0)

    def __str__(self):
        return self.rated

    class Meta:
        ordering = ('rated',)
        # composite index using index_together meta option: 
        unique_together = (('student', 'book'),)
        indexes = [
            models.Index(fields=['student', 'book']),
        ]
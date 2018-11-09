from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Student(models.Model):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    DEPT_CHOICES = (
        ('Computer Science', 'Computer Science'),
        ('Statistics', 'Statistics'),
        ('Electronic Engineering', 'Electronic Engineering'),
        ('Library Science', 'Library Science'),
    )

    SPEC_CHOICES = (
        ('Software Development', 'Software Development'),
        ('System Design', 'System Design'),
        ('System Analysis', 'System Analysis'),
        ('Programming Languages', 'Programming Languages'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('Bayesian Inference', 'Bayesian Inference'),
        ('Nonlinear programming', 'Nonlinear programming'),
        ('Stochastic Programming', 'Stochastic Programming'),
        ('Multivariate Analysis', 'Multivariate Analysis'),
        ('Algorithms Design & Analysis', 'Algorithms Design & Analysis'),
        ('Time Series Analysis', 'Time Series Analysis'),
        ('Regression Analysis', 'Regression Analysis'),
        ('Non Parametric Methods', 'Non Parametric Methods'),
        ('Software engineering & Info processing', 'Software Engineering and Info processing'),
        ('System development', 'System development'),
        ('Computer Apps to Industry', 'Computer Apps to Industry'),
        ('Database design & implementation', 'Database design & implementation'),
        ('Data Communication Networks', 'Data Communication Networks'),
        ('Computer & library service', 'Computer & library service'),
        ('Academic Libraries Administration', 'Academic Libraries Administration'),
        ('Public Libraries Administration', 'Public Libraries Administration'),
        ('Archives $ Records Administration', 'Archives $ Records Administration'),
    )
    fullname = models.CharField(max_length=10, unique=True)
    sex = models.CharField(choices=GENDER_CHOICES, max_length=1)
    age = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(50), MinValueValidator(15)]
     )
    department = models.CharField(choices=DEPT_CHOICES, max_length=200)
    specialization = models.CharField(choices=SPEC_CHOICES, max_length=200)

    def __str__(self):
        return self.fullname


    class Meta:
        ordering = ('fullname',)


class Item(models.Model):
    CAT_CHOICES = (
        ('Computer Science', 'Computer Science'),
        ('Statistics', 'Statistics'),
        ('Electronic Engineering', 'Electronic Engineering'),
        ('Library Science', 'Library Science'),
    )
    SUBCAT_CHOICES = (
        ('Computer Science', 'Computer Science'),
        ('Statistics', 'Statistics'),
        ('Electronic Engineering', 'Electronic Engineering'),
        ('Library Science', 'Library Science'),
    )
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CAT_CHOICES, max_length=50)
    subcategory = models.CharField(choices=SUBCAT_CHOICES, max_length=50)
    keywords = models.CharField(max_length=100)
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
        (5, 5),
    )
    # list(zip(range(0, 6), range(0, 6)))

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rated = models.IntegerField(choices=CHOICES, default=0)

    def __str__(self):
        return self.rated

    class Meta:
        ordering = ('rated',)
        # composite index using index_together meta option:
        unique_together = (('student', 'item'),)
        indexes = [
            models.Index(fields=['student', 'item']),
        ]





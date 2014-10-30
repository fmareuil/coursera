from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Category(models.Model):
    type = models.CharField(max_length=50)


class Session(models.Model):
    first_date = models.DateTimeField()
    last_date = models.DateTimeField()


class Language(models.Model):
    teacher = models.ForeignKey(Teacher)
    name = models.CharField(max_length=50)
    iso = models.CharField(max_length=2)


class Syllabus(models.Model):
    theme = models.CharField(max_length=100)


class Course(models.Model):
    # description of one user
    user = models.ManyToManyField(User, related_name="courses")
    slug = models.SlugField()
    title = models.CharField(max_length=50)
    definition = models.TextField()
    language = models.ForeignKey(Language)
    teacher = models.ManyToManyField(Teacher)
    categories = models.ForeignKey(Category)
    sessions = models.ManyToManyField(Session)
    syllabus = models.ForeignKey(Syllabus)
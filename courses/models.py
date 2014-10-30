from django.db import models


# Create your models here.
class Teacher(models.Model):
    pass


class Category(models.Model):
    pass


class Session(models.Model):
    pass


class Language(models.Model):
    pass


class Course(models.Model):
    # description of one user
    slug = models.SlugField()
    title = models.CharField(max_length=50)
    definition = models.CharField(max_length=50)
    language = models.ForeignKey(Language)
    teacher = models.ManyToManyField(Teacher)
    categories = models.ForeignKey(Category)
    sessions = models.ManyToManyField(Session)

from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Category(models.Model):
    type = models.CharField(max_length=50)

    def __unicode__(self):
        return self.type


class Session(models.Model):
    first_date = models.DateField()
    last_date = models.DateField()

    def __unicode__(self):
        return "%s - %s" % (self.first_date, self.last_date)


class Language(models.Model):
    teacher = models.ForeignKey(Teacher)
    name = models.CharField(max_length=50)
    iso = models.CharField(max_length=2)

    def __unicode__(self):
        return self.name


class Syllabus(models.Model):
    theme = models.CharField(max_length=100)

    def __unicode__(self):
        return self.theme


class Course(models.Model):
    # description of one user
    user = models.ManyToManyField(User, related_name="courses")
    slug = models.SlugField()
    title = models.CharField(max_length=50)
    definition = models.TextField()
    language = models.ManyToManyField(Language)
    teacher = models.ManyToManyField(Teacher)
    categories = models.ManyToManyField(Category)
    sessions = models.ManyToManyField(Session)
    syllabus = models.ManyToManyField(Syllabus)
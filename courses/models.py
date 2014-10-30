from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Category(models.Model):
    pass


class Session(models.Model):
    pass


class Language(models.Model):
    teacher = models.ForeignKey(teacher)
    name = models.CharField(max_length=50)
    iso = models.CharField(max_length=2)


class Course(models.Model):
    # description of one user
    user = models.ManyToManyField(User, related_name="courses")
    slug = models.SlugField()
    title = models.CharField(max_length=50)
    definition = models.CharField(max_length=50)
    language = models.ForeignKey(Language)
    teacher = models.ManyToManyField(Teacher)
    categories = models.ForeignKey(Category)
    sessions = models.ManyToManyField(Session)

    # programme = models.
    def __unicode__(self):
        return self.full_name

    @property
    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name)
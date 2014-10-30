from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Enseignant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Categorie(models.Model):
    pass


class Session(models.Model):
    pass


class Langue(models.Model):
    enseignant = models.ForeignKey(Enseignant)
    name = models.CharField(max_length=50)
    iso = models.CharField(max_length=2)


class Course(models.Model):
    # description of one user
    user = models.ManyToManyField(User, related_name="courses")
    slug = models.SlugField()
    titre = models.CharField(max_length=50)
    definition = models.CharField(max_length=50)
    langue = models.ForeignKey(Langue)
    enseignants = models.ManyToManyField(Enseignant)
    cathegories = models.ForeignKey(Categorie)
    sessions = models.ManyToManyField(Session)

    # programme = models.



    def __unicode__(self):
        return self.full_name

    @property
    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name)
    
    
    

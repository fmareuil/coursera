from django.db import models

# Create your models here.
class Enseignant(models.Model):
    pass

class Categorie(models.Model):
    pass

class Session( models.Model):
    pass

class Langue( models.Model):
    pass

class Course(models.Model):
    # description of one user
    slug = models.SlugField()
    titre = models.CharField(max_length=50)
    definition = models.CharField(max_length=50)
    langue = models.ForeignKey( Langue )
    enseignants = models.ManyToManyField( Enseignant )
    cathegories = models.ForeignKey( Categorie)
    sessions = models.ManyToManyField(Session)
    
    #programme = models.
    

    
    def __unicode__(self):
        return self.full_name
    
    @property
    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name)
    
    
    

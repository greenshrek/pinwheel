from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING,) #When an object referenced by a ForeignKey is deleted, Django will emulate the behavior of the SQL constraint specified by the on_delete argument.
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    #string representation
    def __str__(self):
        return self.name

class AcccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.DO_NOTHING,) #When an object referenced by a ForeignKey is deleted, Django will emulate the behavior of the SQL constraint specified by the on_delete argument.
    date = models.DateField()

    #string representation
    def __str__(self):
        return self.name

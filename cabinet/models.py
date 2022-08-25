from re import T
from django.db import models


class Author(models.Model):
    sur_name = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    age = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='inst_image')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class HastTag(models.Model):
    hash = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, related_name='a_h')

    def __str__(self) -> str:
        return self.hash
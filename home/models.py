from enum import unique
from os import name, path
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import DateField
from datetime import datetime

from django.db.models.fields.related import ForeignKey

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    creationDate = models.DateField()

    def __str__(self):
        return self.username;

class Company(models.Model):
    name = models.CharField(max_length=100)
    revenue = models.IntegerField()
    foundedOnYear = models.IntegerField()

    def __str__(self):
        return self.name
    

class Developer(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    ofCompany = models.ForeignKey(Company, on_delete=CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default="fooCat")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categorie'
    

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default="fooGenre")

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=5, decimal_places=2,null= True, blank= True, )
    description = models.CharField(max_length=500)
    releaseYear = models.IntegerField()
    ratings = models.DecimalField(max_digits=2, decimal_places=1)
    genre = models.ManyToManyField(Genre)
    category = models.ManyToManyField(Category)
    developer = models.ManyToManyField(Developer)
    company = models.ForeignKey(Company, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Update(models.Model):
    name = models.CharField(max_length=100)
    patchNotes = models.CharField(max_length=300)
    ofGame = models.ForeignKey(Game, on_delete=CASCADE)
    date = models.DateField(default=datetime.today)

    def __str__(self):
        return self.name
    

class Award(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    year = models.IntegerField()
    winner = models.ForeignKey(Game, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
class News(models.Model):
    headLine = models.CharField(max_length=100)
    decription = models.CharField(max_length=300)
    ofGame = models.ForeignKey(Game, on_delete=CASCADE,null=True,blank=True)

    def __str__(self):
        return self.headLine
    

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete = SET_NULL,null=True,blank=True)
    ofGame = models.ForeignKey(Game, on_delete = CASCADE)
    title = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)
    publishDate = datetime.today()

    def __str__(self):
        return self.title

class ProTeam(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    prefix = models.CharField(max_length=10)
    ofGame = models.ManyToManyField(Game)

    def __str__(self):
        return self.name

class ProPlayer(models.Model):
    proName = models.CharField(max_length=100)
    aboutPlayer = models.CharField(max_length=300)
    earnings = models.IntegerField()
    user = models.ForeignKey(User, on_delete=SET_NULL,null=True,blank=True)
    team = models.ForeignKey(ProTeam, on_delete=SET_NULL,null=True,blank=True)
    ofGame = models.ForeignKey(Game, on_delete=CASCADE,null=True,blank=True)

    def __str__(self):
        return self.proName
    
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    prizePool = models.IntegerField()
    ofGame = models.ForeignKey(Game, on_delete=SET_NULL,null=True,blank=True)
    description = models.CharField(max_length=300)
    participatingTeams = models.ManyToManyField(ProTeam)
    winnerTeam = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
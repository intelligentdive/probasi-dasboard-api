from django.db import models
from django.contrib.auth.models import User
class District(models.Model):
    name = models.CharField(max_length=100)

class Country(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    # Add more fields as needed

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    founded_date = models.DateField()
    headquarters_location = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name
    
class Expertise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    domain = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ])
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s expertise in {self.domain} ({self.level})"
    
    

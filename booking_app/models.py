from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class Building(models.Model):
    
    #Attributes
    name = models.CharField(max_length=128, unique=True)
    
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Building, self).save(*args, **kwargs)
    
    #class Meta:
        #verbose_name_plural = ''
    
    def __str__(self):
        return self.name
        
class Room(models.Model):
    # ForeignKey
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    
    # Attributes
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128)
    manager = models.CharField(max_length=128)
    
    # Webpage Attributes
    views = models.IntegerField(default=0)
    bookmarked = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Room, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
        
class Date(models.Model):
    # ForeignKey
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    # Attributes
    datelabel = models.CharField(max_length=128)
    
    def __str__(self):
        return self.datelabel
        
class Timeperiod(models.Model):
    # ForeignKey
    date = models.ForeignKey(Date, on_delete=models.CASCADE)

    # Attributes
    timelabel = models.CharField(max_length=128)

    def __str__(self):
        return self.timelabel
        


class UserProfile(models.Model):
    # ForeignKey
    # Links UserProfile to a User model instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Additional attributes
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    # Additional attributes2
#    bookings =
    
    def __str__(self):
        return self.user.username

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    time = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    room = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    
"""
Booking_app models.py
"""
# Test for Fullclanedar API
#class Events(models.Model):
#    even_id = models.AutoField(primary_key=True)
#    event_name = models.CharField(max_length=255,null=True,blank=True)
#    start_date = models.DateTimeField(null=True,blank=True)
#    end_date = models.DateTimeField(null=True,blank=True)
#    event_type = models.CharField(max_length=10,null=True,blank=True)
#
#    def __str__(self):
#        return self.event_name

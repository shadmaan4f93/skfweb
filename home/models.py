from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class Subject(models.Model):
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject


class HomePage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to='images/', blank=True)
    company = models.CharField(max_length=100, blank=True)
    specialize = models.CharField(max_length=100, blank=True)
    companydetail = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    customerfeedback = models.TextField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    linkedin_profile = models.URLField(blank=True)
    twitter_profile = models.URLField(blank=True)
    facebook_profile = models.URLField(blank=True)
    google_profile = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='Anonymous')
    image = models.ImageField(upload_to='images/')
    cv = models.FileField(upload_to='documents/')
    role = models.CharField(max_length=100, default='Software Developer')
    descriptions = models.TextField(blank=True)
    address = models.CharField(max_length=100, default='Not available')
    email = models.CharField(max_length=100, default='Not available')
    phone = models.CharField(max_length=100, default='Not available')
    payratehourly = models.CharField(max_length=100, default='$0')
    payratemonthly = models.CharField(max_length=100, default='$0')
    subjects = ListCharField(
        base_field=models.CharField(max_length=10),
        size=10,
        max_length=(10 * 12)
    )

    def __str__(self):
        return self.name

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='Anonymous')
    logo = models.ImageField(upload_to='logo/')
    weblink = models.URLField(blank=True)
    descriptions = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='Anonymous')
    logo = models.ImageField(upload_to='logo/') 
    descriptions = models.TextField(blank=True)

    def __str__(self):
        return self.name

class UploadedWork(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='Anonymous')
    workuploaddate = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=100, default='Anonymous@example.com')
    srsdoc = models.FileField(upload_to='documents/') 
    descriptions = models.TextField(blank=True)

    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=200)
    school  = models.CharField(max_length=200)
    tel  = models.IntegerField()
    gender  = models.CharField(max_length=200)
    grade = models.IntegerField()
    openid  = models.CharField(max_length=200)
    email  = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='userinfo')



class Merchants(models.Model):
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    tel  = models.IntegerField()
    size = models.CharField(max_length=200)
    openid  = models.CharField(max_length=200)
    email  = models.CharField(max_length=200)
    user_id  = models.ForeignKey(User, on_delete=models.CASCADE,related_name='merchants')
    address  = models.CharField(max_length=200)
    Introduction  = models.CharField(max_length=500)
    headerName  = models.CharField(max_length=200)
    image = models.ImageField(upload_to="papers")


class Job(models.Model):
    name = models.CharField(max_length=200)
    tel  = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Job')
    address  = models.CharField(max_length=200)
    Introduction  = models.CharField(max_length=500)
    image = models.ImageField(upload_to="papers")
    peoplenum  = models.IntegerField()
    paymethod  = models.CharField(max_length=200)
    jobdate  = models.DateField()
    jobtime  = models.TimeField()
    overtime  = models.DateTimeField()
    commission  = models.CharField(max_length=200)
    treatment  = models.IntegerField()
    treatmentType = models.CharField(max_length=200)
    jobtype = models.CharField(max_length=200)
    communicate = models.CharField(max_length=200)
    communicatenum  = models.CharField(max_length=200)


class SignUp(models.Model):
    user_id  = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    merchants_id  = models.ForeignKey(User, on_delete=models.CASCADE,related_name='signup')
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    tel = models.IntegerField()
    signtime = models.DateTimeField()
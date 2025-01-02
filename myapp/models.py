from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    type=models.CharField(max_length=10)

class Trainer(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=30)
    dob=models.DateField()
    place=models.CharField(max_length=20)
    post=models.CharField(max_length=20)
    pin=models.IntegerField()
    district=models.CharField(max_length=20)
    photo=models.CharField(max_length=500)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    aadhaar=models.CharField(max_length=12)
    aadhaarphoto = models.CharField(max_length=500)
    certificate=models.CharField(max_length=500)
    experience=models.CharField(max_length=500)
    qualification=models.CharField(max_length=500)
    status=models.CharField(max_length=500,default='pending')

class User(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=30)
    dob=models.DateField()
    place=models.CharField(max_length=20)
    post=models.CharField(max_length=20)
    pin=models.IntegerField()
    district=models.CharField(max_length=20)
    photo=models.CharField(max_length=500)
    aadhaarphoto = models.CharField(max_length=500)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    aadhaar=models.CharField(max_length=12)
    udid=models.CharField(max_length=18)

class Chat(models.Model):
    date=models.DateField()
    FROM=models.ForeignKey(Login,on_delete=models.CASCADE,related_name="fromid")
    TO=models.ForeignKey(Login,on_delete=models.CASCADE,related_name="toid")
    message=models.CharField(max_length=500)

class Video(models.Model):
    video=models.CharField(max_length=500)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    date=models.DateField()
    TRAINER=models.ForeignKey(Trainer,on_delete=models.CASCADE)

class Review(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    TRAINER=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    VIDEO=models.ForeignKey(Video,on_delete=models.CASCADE)
    review=models.CharField(max_length=200)
    rating=models.CharField(max_length=30)
    date=models.DateField()

class Complaint(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    TRAINER=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=200)
    date=models.DateField()
    status=models.CharField(max_length=20)
    reply=models.CharField(max_length=200)

class Request(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    TRAINER=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    status=models.CharField(max_length=20)
    date=models.DateField()
    description=models.CharField(max_length=300)

class Alphabet(models.Model):
    image=models.CharField(max_length=500)
    alphabet=models.CharField(max_length=200)
    TRAINER = models.ForeignKey(Trainer, on_delete=models.CASCADE)







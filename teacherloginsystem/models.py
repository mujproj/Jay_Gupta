from django.db import models

# Create your models here.
class teacherRegister(models.Model):

    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25)

class questions(models.Model):

    username = models.CharField(max_length=50, default="")
    question1 = models.CharField(max_length=500, default="")
    answer1 = models.CharField(max_length=500, default="")
    options1 = models.CharField(max_length=500, default="")
    question2 = models.CharField(max_length=500, default="")
    answer2 = models.CharField(max_length=500, default="")
    options2 = models.CharField(max_length=500, default="")
    question3 = models.CharField(max_length=500, default="")
    answer3 = models.CharField(max_length=500, default="")
    options3 = models.CharField(max_length=500, default="")
    question4 = models.CharField(max_length=500, default="")
    answer4 = models.CharField(max_length=500, default="")
    options4 = models.CharField(max_length=500, default="")
    question5 = models.CharField(max_length=500, default="")
    answer5 = models.CharField(max_length=500, default="")
    options5 = models.CharField(max_length=500, default="")
    question6 = models.CharField(max_length=500, default="")
    answer6 = models.CharField(max_length=500, default="")
    options6 = models.CharField(max_length=500, default="")
    question7 = models.CharField(max_length=500, default="")
    answer7 = models.CharField(max_length=500, default="")
    options7 = models.CharField(max_length=500, default="")
    question8 = models.CharField(max_length=500, default="")
    answer8 = models.CharField(max_length=500, default="")
    options8 = models.CharField(max_length=500, default="")
    question9 = models.CharField(max_length=500, default="")
    answer9 = models.CharField(max_length=500, default="")
    options9 = models.CharField(max_length=500, default="")
    question10 = models.CharField(max_length=500, default="")
    answer10 = models.CharField(max_length=500, default="")
    options10 = models.CharField(max_length=500, default="")
    studentsid = models.CharField(max_length=500, default="")
    password_for_quiz = models.CharField(max_length=500, default="", unique=True)

class studentdata(models.Model):

    username = models.CharField(max_length=500, default="")
    regNumber = models.CharField(max_length=500, default="")
    password = models.CharField(max_length=500, default="")
    score = models.CharField(max_length=500, default="")
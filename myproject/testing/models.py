from django.db import models

# Create your models here.

class Bdquestions(models.Model):
    fio = models.CharField(max_length=100)
    questions = models.TextField()
    answer1 = models.TextField()
    answer2 = models.TextField()
    trueanswer = models.CharField(max_length=1)

    def __str__(self):
        return self.fio 
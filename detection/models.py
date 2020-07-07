from django.db import models

# Create your models here.


class Post(models.Model):
    file = models.FileField()

    def __str__(self):
        return self.file


class LiveCam(models.Model):
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.date


class Terminate(models.Model):
    stop = models.CharField(max_length=100)

    def __str__(self):
        return self.date


class ImageDetection(models.Model):
    file = models.FileField()

    def __str__(self):
        return self.file

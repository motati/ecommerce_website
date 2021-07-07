from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.fields.files import ImageField
from PIL import Image



class Mobile(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='mobile_pics')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Laptop(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='laptop_pics')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Painting(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='painting_pics')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Canvas(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='canvas_pics')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Clothing(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='clothing_pics')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
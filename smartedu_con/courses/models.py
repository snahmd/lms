from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Kurs Adı", help_text="Kurs Adını Yazınız.")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/abc.jpg")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)


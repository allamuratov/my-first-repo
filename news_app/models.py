from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class News(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", 'Draft'
        Publish = "PB", 'Publish'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300)
    body = models.TextField()
    image = models.ImageField(upload_to='media/news/')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices,
                              default=Status.Draft)


    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.title






from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    image = models.FileField(upload_to='post_image',blank=True)
    birthdate = models.DateField(blank=True,null=True)
    date_create = models.DateField(blank=True)
    date_update = models.DateField(blank=True)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
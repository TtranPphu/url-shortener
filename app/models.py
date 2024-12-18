from django.db import models


# Create your models here.
class Shortened(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=256)
    shortCode = models.CharField(max_length=8)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return self.shortCode + " | " + self.url


class ShortenRequest(models.Model):
    url = url = models.CharField(max_length=256)

    def __str__(self):
        return self.url

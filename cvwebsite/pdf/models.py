from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    summery = models.TextField(max_length=1000, null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255, null=True, blank=True)
    university = models.CharField(max_length=255,null=True, blank=True)
    previous_work = models.TextField(max_length=1000, null=True, blank=True)
    skills = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

class TODO(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
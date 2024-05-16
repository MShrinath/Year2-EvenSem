from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=12, blank=False)

    class Meta:
        db_table = "user_table"
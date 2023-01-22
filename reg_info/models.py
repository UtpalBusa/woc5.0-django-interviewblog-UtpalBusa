from django.db import models

class RegInfo(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    conf_password = models.CharField(max_length=20)
    sel_deg = models.CharField(max_length=25)
    pos = models.CharField(max_length=50)
    grad_year = models.CharField(max_length=10)


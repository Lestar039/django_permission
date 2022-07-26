from django.db import models


class T1(models.Model):
    name = models.CharField(max_length=5)


class T2(models.Model):
    name = models.CharField(max_length=5)


class T3(models.Model):
    name = models.CharField(max_length=5)

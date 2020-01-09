from django.db import models


class Answer(models.Model):
    text = models.CharField(max_length=20)
    image = models.CharField(max_length=500)


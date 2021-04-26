from django.db import models

from django_102.models.player import Player


class Game(models.Model):
    name = models.CharField(max_length=30, blank=False)
    difficulty_level = models.IntegerField(blank=False)
    players = models.ManyToManyField(Player)
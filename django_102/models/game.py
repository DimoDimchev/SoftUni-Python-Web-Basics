from django.db import models

from django_102.models.player import Player


class Game(models.Model):
    DIFFICULTY_LEVEL_CHOICES = (
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('HARD', 'Hard')
    )
    name = models.CharField(max_length=30, blank=False)
    difficulty_level = models.CharField(max_length=6, blank=False, choices=DIFFICULTY_LEVEL_CHOICES)
    players = models.ManyToManyField(Player)
# Generated by Django 3.2 on 2021-04-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_102', '0005_game_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='difficulty_level',
            field=models.IntegerField(choices=[('Easy', 0), ('Meduim', 1), ('Hard', 2)]),
        ),
    ]

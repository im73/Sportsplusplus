# Generated by Django 2.1.7 on 2019-04-16 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0007_match_teamsummary_home_away'),
    ]

    operations = [
        migrations.AddField(
            model_name='match_teamsummary',
            name='home_away',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0007_auto_20210606_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='recommendation.Genre'),
        ),
    ]

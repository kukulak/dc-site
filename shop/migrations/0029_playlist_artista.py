# Generated by Django 2.2.4 on 2019-12-29 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_auto_20191105_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='artista',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

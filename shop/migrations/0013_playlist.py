# Generated by Django 2.2.3 on 2019-09-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_hotel_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('cancion', models.CharField(max_length=100)),
                ('porque', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
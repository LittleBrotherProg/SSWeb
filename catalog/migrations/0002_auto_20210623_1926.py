# Generated by Django 3.2.4 on 2021-06-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='photo_id',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='servis_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
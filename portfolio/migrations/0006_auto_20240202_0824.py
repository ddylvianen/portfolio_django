# Generated by Django 3.2.23 on 2024-02-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20240202_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='image',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='text',
        ),
        migrations.AddField(
            model_name='projects',
            name='img',
            field=models.ImageField(default='default.png', upload_to='images'),
        ),
    ]

# Generated by Django 3.2.23 on 2024-02-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]

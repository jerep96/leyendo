# Generated by Django 3.2.7 on 2021-10-01 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0013_url_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='archivo',
            field=models.FileField(upload_to='static'),
        ),
    ]
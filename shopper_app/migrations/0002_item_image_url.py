# Generated by Django 2.1.3 on 2018-11-08 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopper_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]

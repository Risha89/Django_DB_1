# Generated by Django 4.1 on 2022-08-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneDB', '0007_alter_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(),
        ),
    ]

# Generated by Django 4.1 on 2022-08-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneDB', '0015_alter_phone_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.TextField(max_length=200),
        ),
    ]

# Generated by Django 4.1 on 2022-08-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneDB', '0014_alter_phone_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(max_length=200, upload_to=''),
        ),
    ]

# Generated by Django 3.2 on 2021-05-03 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_alter_album_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='thumbnail',
            field=models.ImageField(upload_to='nralif/album/photo/'),
        ),
    ]

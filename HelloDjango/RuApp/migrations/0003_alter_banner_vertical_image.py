# Generated by Django 3.2.10 on 2022-05-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RuApp', '0002_banner_vertical_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='vertical_image',
            field=models.ImageField(blank=True, null=True, upload_to='Баннер/', verbose_name='Баннер для мобильного'),
        ),
    ]

# Generated by Django 3.2.10 on 2022-05-23 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RuApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='vertical_image',
            field=models.ImageField(default=1, upload_to='Баннер/', verbose_name='Баннер для мобильного'),
            preserve_default=False,
        ),
    ]

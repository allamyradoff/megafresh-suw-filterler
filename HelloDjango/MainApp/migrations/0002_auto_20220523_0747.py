# Generated by Django 3.2.10 on 2022-05-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='image_fo',
            field=models.ImageField(upload_to='kompsurat/', verbose_name='Dördünji surat'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image_one',
            field=models.ImageField(upload_to='kompsurat/', verbose_name='Birinji surat'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image_second',
            field=models.ImageField(upload_to='kompsurat/', verbose_name='Ikinji surat'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image_three',
            field=models.ImageField(upload_to='kompsurat/', verbose_name='Üçinji surat'),
        ),
        migrations.AlterField(
            model_name='footerdesc',
            name='image',
            field=models.ImageField(upload_to='footerdesc/', verbose_name='Surat'),
        ),
    ]

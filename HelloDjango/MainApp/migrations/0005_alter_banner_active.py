# Generated by Django 3.2.10 on 2022-05-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_alter_banner_vertical_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='active',
            field=models.CharField(blank=True, choices=[('active', 'active')], max_length=16, null=True),
        ),
    ]
# Generated by Django 3.2.10 on 2022-05-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_auto_20220528_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='line_one',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Goşmaça'),
        ),
        migrations.AlterField(
            model_name='product',
            name='line_three',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Goşmaça'),
        ),
        migrations.AlterField(
            model_name='product',
            name='line_two',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Goşmaça'),
        ),
    ]

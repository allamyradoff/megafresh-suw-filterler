# Generated by Django 3.2.10 on 2022-05-22 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Harydyň gysgaça berýany')),
                ('desc', models.TextField(verbose_name='Harydyň beýany')),
            ],
            options={
                'verbose_name': 'Haryt barada',
                'verbose_name_plural': 'Harytlar barada',
            },
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Ady')),
                ('mini_desc', models.CharField(max_length=255, verbose_name='Gysgaça beýan')),
                ('desc', models.TextField(verbose_name='Beýan')),
                ('image_one', models.ImageField(upload_to='komp surat/', verbose_name='Birinji surat')),
                ('image_second', models.ImageField(upload_to='komp surat/', verbose_name='Ikinji surat')),
                ('image_three', models.ImageField(upload_to='komp surat/', verbose_name='Üçinji surat')),
                ('image_fo', models.ImageField(upload_to='komp surat/', verbose_name='Dördünji surat')),
            ],
            options={
                'verbose_name': 'Kompaniýa barada',
                'verbose_name_plural': 'Kompaniýalar barada',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='banner')),
                ('image', models.ImageField(upload_to='banner/', verbose_name='Banner')),
                ('active', models.CharField(blank=True, choices=[('active', 'active'), ('no active', 'no active')], default='no_active', max_length=16, null=True)),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Bannerlar',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kategoriýanyň ady')),
                ('slider_number', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=255, unique=True, verbose_name='Çalşyryjy slideriň sany')),
            ],
            options={
                'verbose_name': 'Kategoriýa',
                'verbose_name_plural': 'Kategoriýalar',
            },
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='sertifikat')),
                ('image', models.ImageField(upload_to='certification/', verbose_name='Sertifikat suraty')),
            ],
            options={
                'verbose_name': 'Sertifikat',
                'verbose_name_plural': 'Sertifikatlar',
            },
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Logo')),
                ('logo_mini', models.ImageField(upload_to='logo/', verbose_name='Logo')),
                ('number', models.IntegerField(verbose_name='Telefon nomer')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('map', models.TextField(verbose_name='Karta')),
            ],
            options={
                'verbose_name': 'Kompaniýanyň maglymaty',
                'verbose_name_plural': 'Kompaniýanyň maglymatlary',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Ady')),
                ('location', models.CharField(max_length=255, verbose_name='Ýerleşýän ýeri')),
                ('mobile_number', models.IntegerField(verbose_name='Telefon nomer')),
                ('number', models.IntegerField(verbose_name='Ofis Nomer')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Kontakt',
                'verbose_name_plural': 'Kontaktlar',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('name', models.CharField(max_length=255, verbose_name='Ady')),
                ('message', models.TextField(verbose_name='SMS')),
            ],
            options={
                'verbose_name': 'Gelen Hat',
                'verbose_name_plural': 'Gelen hatlar',
            },
        ),
        migrations.CreateModel(
            name='FooterDesc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Ady')),
                ('desc', models.CharField(max_length=255, verbose_name='Beýany')),
                ('image', models.ImageField(upload_to='footer desc/', verbose_name='Surat')),
            ],
            options={
                'verbose_name': 'Aşakdaky Beýan',
                'verbose_name_plural': 'Aşakdaky Beýanlar',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Harydyň ady')),
                ('image', models.ImageField(upload_to='product/', verbose_name='Harydyň suraty')),
                ('mini_desc', models.CharField(max_length=255, verbose_name='Harydyň gysgaça beýany')),
                ('desc', models.TextField(verbose_name='Harydyň beýany')),
                ('line_one', models.CharField(max_length=255, verbose_name='Goşmaça')),
                ('line_two', models.CharField(max_length=255, verbose_name='Goşmaça')),
                ('line_three', models.CharField(max_length=255, verbose_name='Goşmaça')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.category', verbose_name='Hardydyň kategoriýasy')),
            ],
            options={
                'verbose_name': 'Haryt',
                'verbose_name_plural': 'Harytlar',
            },
        ),
    ]

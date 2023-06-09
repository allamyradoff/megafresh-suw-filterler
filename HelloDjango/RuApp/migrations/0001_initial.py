# Generated by Django 3.2.10 on 2022-05-22 19:27

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
                ('title', models.CharField(max_length=255, verbose_name='Короткая описание продукта')),
                ('desc', models.TextField(verbose_name='Описание продукта')),
            ],
            options={
                'verbose_name': 'О продуте',
                'verbose_name_plural': 'О продуте',
            },
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Имя')),
                ('mini_desc', models.CharField(max_length=255, verbose_name='Короткая описание')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('image_one', models.ImageField(upload_to='komp surat/', verbose_name='Первое фото')),
                ('image_second', models.ImageField(upload_to='komp surat/', verbose_name='Второе фото')),
                ('image_three', models.ImageField(upload_to='komp surat/', verbose_name='Третее фото')),
                ('image_fo', models.ImageField(upload_to='komp surat/', verbose_name='Четвертое фото')),
            ],
            options={
                'verbose_name': 'О компании',
                'verbose_name_plural': 'О компании',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Баннер')),
                ('image', models.ImageField(upload_to='banner/', verbose_name='Баннер')),
                ('active', models.CharField(blank=True, choices=[('active', 'active'), ('no active', 'no active')], default='no_active', max_length=16, null=True)),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slider_number', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=255, unique=True, verbose_name='Слайдер для смены продукта')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Сертификат')),
                ('image', models.ImageField(upload_to='certification/', verbose_name='Сертификат')),
            ],
            options={
                'verbose_name': 'Сертификат',
                'verbose_name_plural': 'Сертификаты',
            },
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Logo')),
                ('logo_mini', models.ImageField(upload_to='logo/', verbose_name='Logo')),
                ('number', models.IntegerField(verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('map', models.TextField(verbose_name='Карта')),
            ],
            options={
                'verbose_name': 'Информация о компании',
                'verbose_name_plural': 'Информация о компании',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Имя')),
                ('location', models.CharField(max_length=255, verbose_name='Расположение')),
                ('mobile_number', models.IntegerField(verbose_name='Мобильный номер')),
                ('number', models.IntegerField(verbose_name='Номер оффиса')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('message', models.TextField(verbose_name='SMS')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомлении',
            },
        ),
        migrations.CreateModel(
            name='FooterDesc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Имя')),
                ('desc', models.CharField(max_length=255, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='footer desc/', verbose_name='Изоброжение')),
            ],
            options={
                'verbose_name': 'Нижнее описание',
                'verbose_name_plural': 'Нижнее описание',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='product/', verbose_name='Изоброжение продукта')),
                ('mini_desc', models.CharField(max_length=255, verbose_name='Короткая описание продукта')),
                ('desc', models.TextField(verbose_name='Описание продукта')),
                ('line_one', models.CharField(max_length=255, verbose_name='Дополнительно')),
                ('line_two', models.CharField(max_length=255, verbose_name='Дополнительно')),
                ('line_three', models.CharField(max_length=255, verbose_name='Дополнительно')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RuApp.category', verbose_name='Категория продута')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]

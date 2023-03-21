# Generated by Django 3.2.10 on 2022-05-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RuApp', '0005_auto_20220523_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutproduct',
            options={'verbose_name': 'О продуте', 'verbose_name_plural': '4. О продуте'},
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'О компании', 'verbose_name_plural': '3. О компании'},
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'Баннер', 'verbose_name_plural': '2. Баннеры'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': '5. Категории'},
        ),
        migrations.AlterModelOptions(
            name='certification',
            options={'verbose_name': 'Сертификат', 'verbose_name_plural': '9. Сертификаты'},
        ),
        migrations.AlterModelOptions(
            name='companyinfo',
            options={'verbose_name': 'Информация о компании', 'verbose_name_plural': '1. Информация о компании'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': '8. Контакты'},
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'Уведомление', 'verbose_name_plural': '10. Уведомлении'},
        ),
        migrations.AlterModelOptions(
            name='footerdesc',
            options={'verbose_name': 'Нижнее описание', 'verbose_name_plural': '7. Нижнее описание'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': '6. Продукты'},
        ),
        migrations.AlterField(
            model_name='banner',
            name='vertical_image',
            field=models.ImageField(blank=True, null=True, upload_to='banner/', verbose_name='Баннер для мобильного'),
        ),
    ]
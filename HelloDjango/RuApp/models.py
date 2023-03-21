
from audioop import maxpp
from email import message
from enum import unique
from django.db import models

class CompanyInfo(models.Model):
    logo = models.ImageField(upload_to="logo/", verbose_name="Logo")
    logo_mini = models.ImageField(upload_to="logo/", verbose_name="Logo")
    number = models.CharField(max_length=20, verbose_name="Номер телефона", blank=True, null=True)
    email = models.EmailField(max_length=50, verbose_name="Email")
    map = models.TextField(verbose_name="Карта")
    
    
    class Meta:
        verbose_name = 'Информация о компании'
        verbose_name_plural = '1. Информация о компании'
    

    def __str__(self):
        return self.email  
    
class AboutUs(models.Model):
    title = models.CharField(max_length=255, verbose_name="Имя")
    mini_desc = models.CharField(max_length=255, verbose_name="Короткая описание")
    desc = models.TextField(verbose_name="Описание")
    image_one = models.ImageField(upload_to="komp_surat/", verbose_name="Первое фото")
    image_second = models.ImageField(upload_to="komp_surat/", verbose_name="Второе фото")
    # image_three = models.ImageField(upload_to="komp_surat/", verbose_name="Третее фото")
    # image_fo = models.ImageField(upload_to="komp_surat/", verbose_name="Четвертое фото")
    
    
    
    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = '3. О компании'
    

    def __str__(self):
        return self.title  

class Category(models.Model):
    
    CHIOCES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
    ] 
    
    name = models.CharField(max_length=255, verbose_name="Название категории")
    slider_number = models.CharField(max_length=255, unique=True, choices=CHIOCES, verbose_name="Слайдер для смены продукта")
    
    
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = '5. Категории'
    

    def __str__(self):
        return self.name  


  
class AboutProduct(models.Model):
    title = models.CharField(max_length=255, verbose_name="Короткая описание продукта")
    desc = models.TextField(verbose_name="Описание продукта")


    class Meta:
        verbose_name = 'О продуте'
        verbose_name_plural = '4. О продуте'
    

    def __str__(self):
        return self.title  
    
    
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    image = models.ImageField(upload_to="product/", verbose_name="Изоброжение продукта")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория продута")
    mini_desc = models.CharField(max_length=255, verbose_name="Короткая описание продукта")
    desc = models.TextField( verbose_name="Описание продукта")
    line_one = models.CharField(max_length=255, verbose_name="Дополнительно", null=True, blank=True)
    line_two = models.CharField(max_length=255, verbose_name="Дополнительно", null=True, blank=True)
    line_three = models.CharField(max_length=255, verbose_name="Дополнительно", null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = '6. Продукты'
    

    def __str__(self):
        return self.name  
    
    
class FooterDesc(models.Model):
    title = models.CharField(max_length=255, verbose_name="Имя")
    desc = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="footer_desc/", verbose_name="Изоброжение")
    
    
    class Meta:
        verbose_name = 'Нижнее описание'
        verbose_name_plural = '7. Нижнее описание'
    

    def __str__(self):
        return self.title  
    

class Contact(models.Model):
    title = models.CharField(max_length=255, verbose_name="Имя")
    location = models.CharField(max_length=255, verbose_name="Расположение")
    mobile_number = models.IntegerField(verbose_name="Мобильный номер")
    number = models.IntegerField(verbose_name="Номер оффиса")
    email = models.EmailField(max_length=50, verbose_name="Email")
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = '8. Контакты'
    

    def __str__(self):
        return self.title  
    
    
class ContactUs(models.Model):
    email = models.EmailField(max_length=50, verbose_name="Email")
    name = models.CharField(max_length=255, verbose_name="Имя")
    message = models.TextField(verbose_name="SMS")
    
    
    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = '10. Уведомлении'
    

    def __str__(self):
        return self.email
    
    
class Banner(models.Model):
    
    ACTIVE = [
        ("active", "active"),
    ]  
        
    name = models.CharField(verbose_name="Баннер", max_length=255)  
    image = models.ImageField(upload_to="banner/", verbose_name="Баннер")
    vertical_image = models.ImageField(upload_to="banner/", verbose_name="Баннер для мобильного", blank=True, null=True)
    active = models.CharField(max_length=16, choices=ACTIVE, blank=True, null=True)
    
    
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = '2. Баннеры'
    

    def __str__(self):
        return self.name
    
    
class Certification(models.Model):
    name = models.CharField(verbose_name="Сертификат", max_length=255)  
    image = models.ImageField(upload_to="certification/", verbose_name="Сертификат")
    
    
    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = '9. Сертификаты'
    

    def __str__(self):
        return self.name
    
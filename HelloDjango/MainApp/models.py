
from audioop import maxpp
from email import message
from enum import unique
from django.db import models

class CompanyInfo(models.Model):
    logo = models.ImageField(upload_to="logo/", verbose_name="Logo")
    logo_mini = models.ImageField(upload_to="logo/", verbose_name="Logo Kici")
    number = models.CharField(max_length=20, verbose_name="Telefon nomer", blank=True, null=True)
    email = models.EmailField(max_length=50, verbose_name="Email")
    map = models.TextField(verbose_name="Karta")
    
    
    class Meta:
        verbose_name = 'Kompaniýanyň maglymaty'
        verbose_name_plural = '1. Kompaniýanyň maglymatlary'
    

    def __str__(self):
        return self.email  
    
class AboutUs(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ady")
    mini_desc = models.CharField(max_length=255, verbose_name="Gysgaça beýan")
    desc = models.TextField(verbose_name="Beýan")
    image_one = models.ImageField(upload_to="kompsurat/", verbose_name="Birinji surat")
    image_second = models.ImageField(upload_to="kompsurat/", verbose_name="Ikinji surat")
    # image_three = models.ImageField(upload_to="kompsurat/", verbose_name="Üçinji surat")
    # image_fo = models.ImageField(upload_to="kompsurat/", verbose_name="Dördünji surat")
    
    
    
    class Meta:
        verbose_name = 'Kompaniýa barada'
        verbose_name_plural = '3. Kompaniýa barada'
    

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
    
    name = models.CharField(max_length=255, verbose_name="Kategoriýanyň ady")
    slider_number = models.CharField(max_length=255, unique=True, choices=CHIOCES, verbose_name="Çalşyryjy slideriň sany")
    
    
    
    class Meta:
        verbose_name = 'Kategoriýa'
        verbose_name_plural = '5. Kategoriýalar'
    

    def __str__(self):
        return self.name  


  
class AboutProduct(models.Model):
    title = models.CharField(max_length=255, verbose_name="Harydyň gysgaça berýany")
    desc = models.TextField(verbose_name="Harydyň beýany")


    class Meta:
        verbose_name = 'Haryt barada'
        verbose_name_plural = '4. Harytlar barada'
    

    def __str__(self):
        return self.title  
    
    
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Harydyň ady")
    image = models.ImageField(upload_to="product/", verbose_name="Harydyň suraty")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Hardydyň kategoriýasy")
    mini_desc = models.CharField(max_length=255, verbose_name="Harydyň gysgaça beýany")
    desc = models.TextField( verbose_name="Harydyň beýany")
    line_one = models.CharField(max_length=255, verbose_name="Goşmaça", null=True, blank=True)
    line_two = models.CharField(max_length=255, verbose_name="Goşmaça", null=True, blank=True)
    line_three = models.CharField(max_length=255, verbose_name="Goşmaça", null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Haryt'
        verbose_name_plural = '6. Harytlar'
    

    def __str__(self):
        return self.name  
    
    
class FooterDesc(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ady")
    desc = models.TextField(verbose_name="Beýany")
    image = models.ImageField(upload_to="footerdesc/", verbose_name="Surat")
    
    
    class Meta:
        verbose_name = 'Aşakdaky Beýan'
        verbose_name_plural = '7. Aşakdaky Beýanlar'
    

    def __str__(self):
        return self.title  
    

class Contact(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ady")
    location = models.CharField(max_length=255, verbose_name="Ýerleşýän ýeri")
    mobile_number = models.IntegerField(verbose_name="Telefon nomer")
    number = models.IntegerField(verbose_name="Ofis Nomer")
    email = models.EmailField(max_length=50, verbose_name="Email")
    
    class Meta:
        verbose_name = 'Kontakt'
        verbose_name_plural = '8. Kontaktlar'
    

    def __str__(self):
        return self.title  
    
    
class ContactUs(models.Model):
    email = models.EmailField(max_length=50, verbose_name="Email")
    name = models.CharField(max_length=255, verbose_name="Ady")
    message = models.TextField(verbose_name="SMS")
    
    
    class Meta:
        verbose_name = 'Gelen Hat'
        verbose_name_plural = '10. Gelen hatlar'
    

    def __str__(self):
        return self.email
    
    
class Banner(models.Model):
    
    ACTIVE = [
        ("active", "active"),
    ]  
        
    name = models.CharField(verbose_name="banner", max_length=255)  
    image = models.ImageField(upload_to="banner/", verbose_name="Banner")
    vertical_image = models.ImageField(upload_to="banner/", verbose_name="Banner telefon üçin", blank=True, null=True)
    active = models.CharField(max_length=16, choices=ACTIVE, blank=True, null=True)
    
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = '2. Bannerlar'
    

    def __str__(self):
        return self.name
    
    
class Certification(models.Model):
    name = models.CharField(verbose_name="sertifikat", max_length=255)  
    image = models.ImageField(upload_to="certification/", verbose_name="Sertifikat suraty")
    
    
    class Meta:
        verbose_name = 'Sertifikat'
        verbose_name_plural = '9. Sertifikatlar'
    

    def __str__(self):
        return self.name
    
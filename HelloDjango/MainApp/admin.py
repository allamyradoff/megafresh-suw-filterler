from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'image']



admin.site.register(CompanyInfo)
admin.site.register(AboutUs)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(AboutProduct)
admin.site.register(FooterDesc)
admin.site.register(Contact)
admin.site.register(ContactUs)
admin.site.register(Banner)
admin.site.register(Certification)
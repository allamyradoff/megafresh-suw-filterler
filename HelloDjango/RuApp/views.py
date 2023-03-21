from django.shortcuts import render, redirect
from RuApp.form import ContactUsForm
from RuApp.models import *



def index(request):
    company_info = CompanyInfo.objects.all()[:1]
    about_us = AboutUs.objects.all()[:1]
    category = Category.objects.all()
    about_product = AboutProduct.objects.all()[:1]
    product = Product.objects.order_by('-id')
    footer_desc = FooterDesc.objects.all()[:1]
    contact = Contact.objects.all()
    contact_us = ContactUs.objects.all()
    banner = Banner.objects.all()[:4]
    certification = Certification.objects.all()
    
    form = ContactUsForm()
    if request.method=="POST":
        form=ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Ruindex')
    
    
    context = {
        "company_info":company_info,
        "category":category,
        "banner":banner,
        "about_us":about_us,
        "about_product":about_product,
        "product":product,
        "footer_desc":footer_desc,
        "contact":contact,
        "contact_us":contact_us,
        "certification":certification,    
        "form":form
    }
    return render(request, 'Ruindex.html', context)





from django import forms
from RuApp.models import ContactUs



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["email", "name", "message"]
        
        
        widgets = {
            "email":forms.TextInput(attrs={'class':"form-control", 'placeholder':"Email"}),
            "name":forms.TextInput(attrs={'class':"form-control", 'placeholder':"Имя"}),
            "message":forms.Textarea(attrs={'class':"form-control", 'placeholder':"Сообщение"}),
        }
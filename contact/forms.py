# contact/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'input__control', 'placeholder': 'Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input__control', 'placeholder': 'Email'}))
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'input__control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'input__control textarea', 'placeholder': 'Message', 'rows': 10}), required=True)

from django.shortcuts import render
from contact.forms import ContactForm

# Create your views here.
def index(request):
    form = ContactForm()
    
    return render(request,'index.html',{'form': form})
# contact/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Create email content
            email_subject = f"Contact Me {subject}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Send email
            send_mail(
                subject=email_subject,
                message=email_message,
                from_email=email,  # This will be the user's email
                recipient_list=['markcharleskojo@gmail.com'],  # Your email address to receive the form
                fail_silently=False,
            )

            # Return success response
            return JsonResponse({'success': True, 'message': 'Message sent successfully!'})

        # If the form is not valid, return a response with errors
        return JsonResponse({'success': False, 'errors': form.errors})

    
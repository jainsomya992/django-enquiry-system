from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Enquiry
from .forms import EnquiryForm
from .services.whatsapp import send_whatsapp_alert, send_whatsapp_user_confirmation

def home(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save()
            
            # Send Email Notification
            subject = f"New Enquiry from {enquiry.name}"
            message = f"""
            New Enquiry Received:
            
            Name: {enquiry.name}
            Email: {enquiry.email}
            Phone: {enquiry.phone}
            
            Message:
            {enquiry.message}
            """
            
            try:
                send_mail(
                    subject,
                    message,
                    'admin@example.com', # From email
                    ['admin@example.com'], # To email
                    fail_silently=False,
                )

                # Send Auto-Reply to User
                reply_subject = "We received your enquiry"
                reply_message = f"""
                Dear {enquiry.name},

                Thank you for contacting us. We have received your enquiry and our team will get back to you shortly.

                Best regards,
                The Team
                """
                
                send_mail(
                    reply_subject,
                    reply_message,
                    'admin@example.com', # From email
                    [enquiry.email], # To user email
                    fail_silently=False,
                )
            except Exception as e:
                # Log the error but don't stop the user flow
                print(f"Error sending email: {e}")

            # Send WhatsApp Alert using Helper Service
            send_whatsapp_alert(enquiry)
            send_whatsapp_user_confirmation(enquiry)

            messages.success(request, 'Thank you! Your enquiry has been submitted successfully.')
            return redirect('home')
    else:
        form = EnquiryForm()

    return render(request, 'core/home.html', {'form': form})

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')




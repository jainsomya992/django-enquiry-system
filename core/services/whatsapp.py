from django.conf import settings
from twilio.rest import Client

def send_whatsapp_alert(enquiry):
    """
    Sends a WhatsApp alert to the admin when a new enquiry is received.
    Fails silently if credentials are missing or incorrect to avoid breaking the user flow.
    """
    try:
        # Check if settings are configured
        if not all([settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN, 
                   settings.TWILIO_WHATSAPP_FROM, settings.ADMIN_WHATSAPP_NUMBER]):
            print("Twilio settings missing. WhatsApp alert skipped.")
            return

        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        message_body = (
            f"🔔 *New Enquiry Received*\n\n"
            f"*Name:* {enquiry.name}\n"
            f"*Email:* {enquiry.email}\n"
            f"*Phone:* {enquiry.phone}\n\n"
            f"*Message:*\n{enquiry.message}"
        )

        message = client.messages.create(
            from_=settings.TWILIO_WHATSAPP_FROM,
            body=message_body,
            to=settings.ADMIN_WHATSAPP_NUMBER
        )
        print(f"WhatsApp alert sent successfully: {message.sid}")

    except Exception as e:
        print(f"Error sending WhatsApp alert: {e}")

def send_whatsapp_user_confirmation(enquiry):
    """
    Sends a WhatsApp confirmation to the user.
    Fails silently if credentials are missing or incorrect.
    """
    try:
        # Check if settings are configured
        if not all([settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN, settings.TWILIO_WHATSAPP_FROM]):
            print("Twilio settings missing. User confirmation skipped.")
            return

        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        message_body = (
            f"Hi {enquiry.name} 👋,\n\n"
            f"Thank you for contacting us! We have received your enquiry regarding:\n"
            f"\"{enquiry.message[:50]}...\"\n\n"
            f"Our team will get back to you shortly.\n\n"
            f"Best regards,\n"
            f"The Team"
        )

        # For Sandbox, we usually need 'whatsapp:' prefix. 
        # Assuming user inputs a full number or local. 
        # In a real app, strict E.164 formatting is required.
        # Here we just blindly prepend 'whatsapp:' and hope the user entered a valid sandbox number format.
        to_number = f"whatsapp:{enquiry.phone}"

        message = client.messages.create(
            from_=settings.TWILIO_WHATSAPP_FROM,
            body=message_body,
            to=to_number
        )
        print(f"WhatsApp confirmation sent successfully: {message.sid}")

    except Exception as e:
        print(f"Error sending WhatsApp confirmation: {e}")

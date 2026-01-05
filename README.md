# Django Enquiry System

A production-style Django backend application that handles user enquiries and sends real-time notifications to admins and users via **Email (SMTP)** and **WhatsApp (Twilio)**.

This project demonstrates clean Django architecture, secure environment-based configuration, and real-world third-party integrations.

---

## ✨ Features

- User enquiry form with server-side validation
- Admin notification via email (SMTP)
- User auto-reply email confirmation
- Admin WhatsApp alert using Twilio
- User WhatsApp confirmation (best-effort, sandbox-safe)
- Secure `.env`-based configuration
- Clean service-layer architecture
- Django Admin panel for enquiry management

---

##  Tech Stack

- **Backend:** Django, Python
- **Database:** SQLite (development)
- **Email:** SMTP (Gmail)
- **Messaging:** Twilio WhatsApp Sandbox
- **Environment Management:** `.env`
- **Frontend:** HTML, CSS (Django templates)

---

##  Project Structure
django-enquiry-system/
├── core/
│ ├── services/
│ │ └── whatsapp.py
│ ├── templates/
│ ├── forms.py
│ ├── models.py
│ ├── views.py
│ └── urls.py
├── enquiry_site/
│ └── settings.py
├── manage.py
├── requirements.txt
└── README.md


---

##  Setup Instructions

# Clone the repository

git clone https://github.com/jainsomya992/django-enquiry-system.git
cd django-enquiry-system

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows

# install dependencies
pip install -r requirements.txt

## Create a .env file
# Email (SMTP)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password
DEFAULT_FROM_EMAIL=your_email@gmail.com

# Twilio WhatsApp
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxx
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
ADMIN_WHATSAPP_NUMBER=whatsapp:+91XXXXXXXXXX

# run migrations
python manage.py migrate

# create superuser
python manage.py createsuperuser

# start the dev server
python manage.py runserver

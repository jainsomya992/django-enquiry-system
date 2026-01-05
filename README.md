# Django Enquiry System

A production-ready Django backend application designed for reliable enquiry management. It features secure form handling, dual-channel notifications (Email + WhatsApp), and a robust service-layer architecture.

This project demonstrates meaningful engineering practices including strict validation, environment-based configuration, and seamless integration with third-party APIs (Twilio, Gmail SMTP).

---

## ✨ Features

### Core Functionality
- **Enquiry Management**: Secure contact form with server-side validation for phone numbers (10 digits) and emails.
- **Admin Dashboard**: Built-in Django admin interface to view and manage enquiries.

### Real-Time Notifications
- **Admin Email Alert**: Immediate notification via SMTP (Gmail) with enquiry details.
- **User Auto-Reply**: Branded confirmation email sent to the user.
- **WhatsApp Admin Alert**: Instant notification to the admin's phone via Twilio API.
- **WhatsApp User Confirmation**: formatted "Thank You" message sent to the user's WhatsApp (Sandbox compatible).


---

## 🛠 Tech Stack

- **Backend**: Django 5, Python 3.12
- **Database**:  PostgreSQL (Supported via Env)
- **Email Service**: SMTP (Gmail)
- **Messaging Service**: Twilio WhatsApp API
- **Frontend**: Django Templates, Vanilla CSS (No frameworks)

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/jainsomya992/django-enquiry-system.git
cd django-enquiry-system
```

### 2. Environment Setup
Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### 3. Configuration (.env)
Create a `.env` file in the project root. Copy the structure below and fill in your details:

```ini
# --- Email Configuration (SMTP) ---
# Switch 'console' to 'smtp' to send real emails
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
DEFAULT_FROM_EMAIL=your_email@gmail.com

# --- Twilio WhatsApp Configuration ---
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
ADMIN_WHATSAPP_NUMBER=whatsapp:+91xxxxxxxxxx

# --- Database Configuration (PostgreSQL) ---

POSTGRES_DB=enquiry_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### 4. Database Setup
Apply migrations to initialize the database:
```bash
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** to see the application.

---

## 🧪 Testing Features

### Email Testing
- **Dev Mode**: If you comment out the SMTP settings or set `EMAIL_BACKEND` to `console`, emails will print to your terminal.
- **Prod Mode**: With valid Gmail App Credentials, emails will be delivered to real inboxes.

### WhatsApp Testing (Twilio Sandbox)
1. Join the Twilio Sandbox by sending the join code (e.g., `join <word>`) to the Twilio number.
2. **Crucial**: For the **User Auto-Reply** to work during testing, the phone number entered in the form *must also have joined* the Sandbox.

### PostgreSQL Switch
1. Create a Postgres database (e.g., `enquiry_db`).
2. Uncomment the `POSTGRES_` variables in `.env`.
3. Restart the server. Django will connect to Postgres.

---

## 📂 Project Structure

```
django-enquiry-system/
├── core/
│   ├── services/       # Business logic (WhatsApp)
│   ├── static/         # CSS files
│   ├── templates/      # HTML files (About, Services, Home)
│   ├── forms.py        # EnquiryForm validation
│   ├── models.py       # DB Schema
│   └── views.py        # Request handling
├── enquiry_site/
│   └── settings.py     # Config (Env loading, DB logic)
├── .env                # Secrets (GitIgnored)
└── requirements.txt    # Dependencies
```

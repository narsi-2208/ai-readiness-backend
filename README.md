# AI Readiness Backend (Django REST API)

This repository contains the **backend service** for the **AI Readiness Assessment Platform**. It is built using **Django** and **Django REST Framework (DRF)** and is responsible for handling assessments, scoring logic, feedback generation, PDF reports, and email delivery (SMTP / Microsoft Graph).

---

## 🚀 Features

- AI Readiness assessment questionnaire
- Scoring & maturity-level calculation
- Personalized feedback generation
- PDF report generation
- Email delivery (SMTP & Microsoft Graph support)
- RESTful APIs for frontend integration
- Admin dashboard for internal management

---

## 🧱 Tech Stack

- **Backend Framework:** Django 5.x
- **API Layer:** Django REST Framework
- **Database:** SQLite (local) / PostgreSQL (production-ready)
- **Authentication:** Django Admin / API-based
- **Email:**
  - Microsoft Graph API
  - SMTP (App Password based)
- **PDF Generation:** ReportLab / custom renderer
- **Environment Management:** python-dotenv

---

## 📁 Project Structure

```
ai-readiness-backend/
│── .env                     # Environment variables (NOT committed)
│── .gitignore
│── db.sqlite3               # Local DB (dev only)
│── manage.py
│── requirements.txt
│
├── ai_backend/               # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── ai_readiness/             # Core application
    ├── admin.py              # Admin registrations
    ├── apps.py
    ├── models.py             # Database models
    ├── serializers.py        # DRF serializers
    ├── views.py              # API views
    ├── urls.py               # App routes
    ├── scoring.py            # AI readiness scoring logic
    ├── feedback.py           # Feedback & insights logic
    ├── questions_config.py   # Assessment questions config
    ├── pdf_report.py         # PDF generation
    ├── emails.py             # SMTP email logic
    ├── graph_email.py        # Microsoft Graph email logic
    └── migrations/
```

---

## ⚙️ Setup Instructions (Local Development)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-org>/ai-readiness-backend.git
cd ai-readiness-backend
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv ai_env
ai_env\Scripts\activate  # Windows
# source ai_env/bin/activate  # macOS/Linux
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=*

# Email (SMTP)
EMAIL_HOST=smtp.office365.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=assist@yourdomain.com
EMAIL_HOST_PASSWORD=your-app-password

# Microsoft Graph
TENANT_ID=xxxx
CLIENT_ID=xxxx
CLIENT_SECRET=xxxx
GRAPH_SENDER_EMAIL=assist@yourdomain.com
```

> ⚠️ Never commit `.env` to GitHub

---

### 5️⃣ Run Migrations

```bash
python manage.py migrate
```

---

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

### 7️⃣ Run Development Server

```bash
python manage.py runserver
```

Backend will be available at:
```
http://127.0.0.1:8000/
```

---

## 🔗 API Endpoints (High Level)

| Method | Endpoint | Description |
|------|---------|------------|
| POST | /api/assessment/start/ | Create new assessment |
| POST | /api/assessment/submit/ | Submit answers |
| GET | /api/assessment/<id>/ | Get assessment result |
| POST | /api/assessment/email/ | Send report email |

> Detailed API documentation can be added via Swagger / Postman collection.

---

## 🧠 Scoring Logic

- Each question maps to a maturity dimension
- Weighted scoring model
- Final readiness level:
  - Beginner
  - Intermediate
  - Advanced
  - AI-Driven

Logic implemented in:
```
ai_readiness/scoring.py
```

---

## 📄 PDF Report Generation

- Executive summary
- Dimension-wise score breakdown
- Recommendations
- Visual indicators

Implemented in:
```
ai_readiness/pdf_report.py
```

---

## 📧 Email Delivery Options

### Option 1: SMTP (App Password)
- Simple
- Suitable for low volume
- Uses Outlook / Office365 SMTP

### Option 2: Microsoft Graph API (Recommended)
- Secure OAuth2
- Enterprise-grade
- No password usage

Email logic files:
```
ai_readiness/emails.py
aI_readiness/graph_email.py
```

---

## 🔐 Security Best Practices

- `.env` for secrets
- App passwords instead of real passwords
- OAuth2 for Graph API
- Admin access restricted
- Production should use:
  - PostgreSQL
  - HTTPS
  - Gunicorn / Uvicorn

---

## 🚢 Deployment Notes

Recommended production stack:

- AWS EC2 / ECS / Lambda
- PostgreSQL (RDS)
- Nginx + Gunicorn
- Azure AD App for Graph API

---

## 🧪 Testing

```bash
python manage.py test
```

---

## 🤝 Contribution Guidelines

1. Fork the repo
2. Create feature branch
3. Commit with clear messages
4. Open Pull Request

---

## 📜 License

This project is proprietary and intended for internal or client use.

---

## 📞 Support

For issues or enhancements, contact the backend team or raise a GitHub Issue.

---

### ✅ Maintained by
**ForgeByte AI**


# Blog Website (Django 5.x)

A Django-based blog application with simple post listing and detail pages.  
Tech: Django 5.x, SQLite (development). Ready for PostgreSQL in production.

## Quick start (local)
1. Create virtualenv:
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows

2. Install deps:
   pip install -r requirements.txt

3. Apply migrations:
   python manage.py migrate

4. Create superuser:
   python manage.py createsuperuser

5. Run server:
   python manage.py runserver

Open http://127.0.0.1:8000

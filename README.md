# AI Medical Appointment Assistant

A comprehensive full-stack web application for managing medical appointments, symptom checking, and AI-powered healthcare assistance.

## Features

- User Authentication (Registration, Login, Logout)
- Patient and Doctor Management
- Appointment Booking System
- AI Symptom Checker
- Doctor Recommendation System
- AI Chatbot for Healthcare Queries
- Admin Dashboard
- Notification System

## Tech Stack

- Backend: Python Django
- API: Django REST Framework
- Database: SQLite (default, can be changed to MySQL)
- Frontend: HTML, CSS, Bootstrap, JavaScript
- AI: OpenAI API (optional, with fallback to keyword matching)

## Setup Instructions

1. **Clone or Download the Project**
   ```
   cd path/to/project
   ```

2. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Run Migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser (Admin)**
   ```
   python manage.py createsuperuser
   ```

5. **Run the Development Server**
   ```
   python manage.py runserver
   ```

6. **Access the Application**
   - Frontend: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/
   - API Endpoints: http://127.0.0.1:8000/api/

## API Endpoints

- `/api/users/patients/` - Patient management
- `/api/doctors/doctors/` - Doctor management
- `/api/appointments/appointments/` - Appointment management
- `/api/symptoms/symptoms/` - Symptom checking
- `/api/chatbot/chats/` - Chat history
- `/api/notifications/notifications/` - Notifications

## Sample Data

To add sample data, you can use the Django admin panel or create a management command.

## Configuration

- For OpenAI API, set the `OPENAI_API_KEY` environment variable.
- Database settings can be changed in `settings.py`.

## Project Structure

```
ai_medical_assistant/
├── ai_medical_assistant/  # Main project settings
├── main/                  # Home and dashboard views
├── users/                 # User and patient management
├── doctors/               # Doctor management
├── appointments/          # Appointment booking
├── symptoms/              # AI symptom checker
├── chatbot/               # AI chatbot
├── notifications/         # Notification system
├── templates/             # HTML templates
├── static/                # CSS, JS, images
├── manage.py
├── requirements.txt
└── README.md
```

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is open-source and available under the MIT License.
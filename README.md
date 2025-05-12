# Remind-Me-Later (Flask API)

This is a simple Flask-based REST API for storing reminders. It accepts a date, time, message, and method (SMS or Email), and saves the reminder data to a local SQLite database.

---

## 🚀 Features

- Accepts reminder data via POST request
- Stores data in SQLite database (`reminders.db`)
- Designed to work with a JavaScript frontend
- Supports methods: `email` or `sms`
- Easily extendable for future delivery methods

---

## 📩 API Endpoint

### POST `/api/reminder`

Accepts a JSON payload and stores the reminder in the database.

#### 🔹 Example Request Body:
```json
{
  "date": "2025-05-15",
  "time": "14:30",
  "message": "Test reminder",
  "method": "email"
}

**Example Success Response:**
{
  "message": "Reminder saved successfully"
}

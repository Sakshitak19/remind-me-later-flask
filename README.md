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

## **How to Run Locally**  
**1. Clone this repository:**  
git clone https://github.com/your-username/remind-me-later-flask.git  
cd remind-me-later-flask  

**2. Create and activate a virtual environment:**  
Create virtual environment  
python -m venv venv  

Activate on Windows  
venv\Scripts\activate  

Activate on macOS/Linux  
source venv/bin/activate  

**3. Install dependencies:**  
pip install -r requirements.txt  

**4. Run the Flask app:**   
python app.py  

## **Testing**  
Use Postman or any API testing tool to send a POST request to:  
http://127.0.0.1:5000/api/reminder  

## **Tools Used**  
Python 3  
Flask  
Flask SQLAlchemy  
SQLite  
Postman (for testing)  

##  **Project Structure**    
remind_me_later_flask/  
├── app.py  
├── config.py  
├── models.py  
├── requirements.txt  
├── reminders.db  ← auto-created  

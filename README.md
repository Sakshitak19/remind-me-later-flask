# Remind-Me-Later (Flask API)  

This is a simple Flask-based REST API for storing reminders. It accepts a date, time, message, and method (SMS or Email) and saves the reminder data to a local SQLite database.  

## Features  

- Accepts reminder data via POST request  
- Stores data in SQLite database (`reminders.db`)  
- Designed to work with a JavaScript frontend  
- Supports methods: `email` or `sms`  
- Easily extendable for future delivery methods  

## API Endpoint  

### POST `/api/reminder`  

Accepts a JSON payload and stores the reminder in the database.  

#### Example Request Body:  
```json  
{  
  "date": "2025-05-15",  
  "time": "14:30",  
  "message": "Test reminder",  
  "method": "email"  
}```

## Example Success Response:

{  
  "message": "Reminder saved successfully"  
}  

## How to Run Locally

### Clone this repository:
git clone https://github.com/your-username/remind-me-later-flask.git
cd remind-me-later-flask
### Create and activate a virtual environment:
python -m venv venv  
Windows:  
venv\Scripts\activate  
macOS/Linux:  
source venv/bin/activate
### Install dependencies:
pip install -r requirements.txt
### Run the app:
python app.py
### Use Postman or any API client to test the endpoint:  
http://127.0.0.1:5000/api/reminder

## Tools Used  
Python 3  
Flask  
Flask SQLAlchemy  
SQLite  

## Testing  
This API was tested using [Postman](https://www.postman.com/), a tool for sending HTTP requests and verifying responses.  

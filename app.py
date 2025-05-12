from flask import Flask, request, jsonify
from config import Config
from models import db, Reminder

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Route for the root URL
@app.route('/')
def home():
    return "Welcome to the Remind Me Later API!"

# API endpoint to create a reminder
@app.route('/api/reminder', methods=['POST'])
def create_reminder():
    data = request.get_json()
    date = data.get('date')
    time = data.get('time')
    message = data.get('message')
    method = data.get('method')

    # Ensure all required fields are provided
    if not all([date, time, message, method]):
        return jsonify({'error': 'Missing required fields'}), 400

    # Create new reminder
    reminder = Reminder(date=date, time=time, message=message, method=method)
    db.session.add(reminder)
    db.session.commit()

    return jsonify({'message': 'Reminder saved successfully'}), 201


# Run the Flask app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates the database and tables
    app.run(debug=True)

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/contact', methods=['POST'])
def contact():
    # Get form data from request
    data = request.get_json()
    
    # Construct email content using form data
    html_content = f"""
    <strong>Uusi yhteydenotto:</strong><br>
    Name: {data['name']}<br>
    Email: {data['email']}<br>
    Phone: {data.get('phone', 'N/A')}<br>
    Message: {data['message']}
    """
    
    message = Mail(
        from_email='info@pohjosenpaja.fi',
        to_emails='jamihyv@gmail.com',
        subject='Uusi yhteydenotto henkilöltä: ' + data['name'],
        html_content=html_content)
    
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        print(str(e))
        return jsonify({'error': 'Failed to send email'}), 500
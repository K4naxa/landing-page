import os
import smtplib
from flask import Flask, request, jsonify, send_file, render_template, send_from_directory
from flask_cors import CORS
from email.message import EmailMessage
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_folder="frontend-dist", template_folder="frontend-dist")
CORS(app)

# Recaptcha validation
@app.route('/api/captcha', methods=['POST'])
def verify_captcha():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({'status': 'preflight'})
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    
    data = request.get_json()
    token = data.get('recaptcha_token')
    
    if not token:
        return jsonify({'error': 'Missing reCAPTCHA token'}), 400
    
    # Verify with Google's reCAPTCHA API
    secret_key = os.getenv('RECAPTCHA_SECRET_KEY')
    response = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={
            'secret': secret_key,
            'response': token
        }
    )
    result = response.json()
    
    # Check if reCAPTCHA was successful and meets your threshold
    if result.get('success') and result.get('score', 0) >= 0.5 and result.get('action') == 'contact':
        return jsonify({'success': True}), 200
    else:
        return jsonify({'error': 'reCAPTCHA verification failed'}), 400
    
# CV download endpoint
@app.route('/api/cv', methods=['POST'])
def get_cv():
    data = request.get_json()
    token = data.get('recaptcha_token')

    if not token:
        return jsonify({'error': 'Missing reCAPTCHA token'}), 400

    # Verify with Google's reCAPTCHA API
    secret_key = os.getenv('RECAPTCHA_SECRET_KEY')
    response = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={
            'secret': secret_key,
            'response': token
        }
    )
    result = response.json()

    # Validate reCAPTCHA response
    if result.get('success') and result.get('score', 0) >= 0.5 and result.get('action') == 'cv_download':
        # Return the CV file
        cv_path = os.path.join(os.getcwd(), "protected", "cv.pdf")
        return send_file(cv_path, mimetype='application/pdf', as_attachment=False)

    return jsonify({'error': 'reCAPTCHA verification failed'}), 400

# Contact form submission
@app.route('/api/contact', methods=['POST'])
def contact():
    # Get form data from request
    data = request.get_json()
    
    # Check for required fields
    required_fields = ['name', 'email', 'subject', 'message']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Construct email content using form data
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 20px auto; padding: 30px; background: #f8f9fa; }}
        .header {{ 
            background: #004aad; 
            color: white;
            padding: 20px;
            border-radius: 5px 5px 0 0;
            margin-bottom: 25px;
        }}
        .section {{ 
            background: white;
            padding: 20px;
            margin-bottom: 15px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }}
        .label {{ 
            color: #666; 
            font-size: 0.9em;
            margin-bottom: 5px;
            display: block;
        }}
        .value {{ 
            font-size: 1.1em;
            margin-bottom: 15px;
        }}
        .message-content {{
            white-space: pre-wrap;
            background: #fff8e1;
            padding: 15px;
            border-left: 3px solid #ffd700;
            margin-top: 10px;
        }}
    </style>
    </head>
    <body>
    <div class="container">
        <div class="header">
            <h2 style="margin: 0;">📬 Uusi yhteydenotto</h2>
        </div>
        
        <div class="section">
            <div class="label">Lähettäjä</div>
            <div class="value">
                {data['name']}<br>
                <a href="mailto:{data['email']}" style="color: #004aad; text-decoration: none;">
                    {data['email']}
                </a>
            </div>
            
            <div class="label">Aihe</div>
            <div class="value" style="color: #004aad; font-weight: 500;">
                {data.get('subject', 'Ei aihetta')}
            </div>
            
            <div class="label">Viesti</div>
            <div class="message-content">
                {data['message']}
            </div>
        </div>
        
        <div style="text-align: center; color: #666; font-size: 0.9em; margin-top: 25px;">
            Tämä viesti lähetettiin Pohjosen Pajan kontaktilomakkeen kautta
        </div>
    </div>
    </body>
    </html>
    """

    # Create email message
    msg = EmailMessage()
    msg['From'] = os.environ.get('FROM_EMAIL')
    msg['To'] = os.environ.get('TO_EMAIL')
    msg['Subject'] = data.get('subject', 'No Subject')
    msg.set_content(html_content, subtype='html')

    try:
        # Get SMTP configuration from environment variables
        smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(os.environ.get('SMTP_PORT', 587))
        smtp_user = os.environ.get('SMTP_USER')
        smtp_password = os.environ.get('SMTP_PASSWORD')

        # Send email using SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        print(f'SMTP error: {str(e)}')
        return jsonify({'error': 'Failed to send email'}), 500


@app.route("/")
def serve_vue_app():
    return render_template("index.html")

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)
    
    

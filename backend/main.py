import os
import requests
import smtplib
from fastapi import FastAPI, HTTPException, Request
from email.message import EmailMessage
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()


# validate_recaptcha function to validate the reCAPTCHA tokens with Google reCAPTCHA API
async def validate_recaptcha(token: str, action: str):
    # Check if Recaptcha token is provided  
    if not token:
        # Return an error if the token is missing
        raise HTTPException(status_code=400, detail="Missing reCAPTCHA token")      
     
    # Validate the reCAPTCHA token with Google reCAPTCHA API      
    secret_key = os.getenv("RECAPTCHA_SECRET_KEY")
    response = requests.post('https://www.google.com/recaptcha/api/siteverify',
                             data={'secret': secret_key, 'response': token})
    
    result = response.json()
    
    # Check if the reCAPTCHA verification was successful, the score is above 0.5 and the action is cv_download 
    if result.get('success') and result.get('score') >= 0.5 and result.get('action') == action:
        return True
    else:
        raise HTTPException(status_code=403, detail="reCAPTCHA verification failed")
    

########### REST API Endpoints ###########

# class for the request body of the /api/cv endpoint
class RecaptchaRequest(BaseModel):
    recaptcha_token: str
    
@app.post("/api/cv")
async def get_cv(data: RecaptchaRequest):
    recapthcaToken = data.recaptcha_token
    action = "cv_download"
    
    # Validate the reCAPTCHA token with Google reCAPTCHA API
    if await validate_recaptcha(recapthcaToken, action):
        cv_path = os.path.join(os.getcwd(), "protected", "cv.pdf")
        return FileResponse(cv_path, media_type='application/pdf')
    else:
        raise HTTPException(status_code=403, detail="reCAPTCHA verification failed")
        
    
    

class ContactRequest(BaseModel):
    name: str
    email: str
    subject: str
    message: str
    recaptcha_token: str

@app.post("/api/contact")
async def send_contact_email(data: ContactRequest):
    
    recaptchaToken = data.recaptcha_token
    action = "contact"
    
    # return an error if the reCAPTCHA verification fails
    if not await validate_recaptcha(recaptchaToken, action):
        raise HTTPException(status_code=403, detail="reCAPTCHA verification failed")
    
    
    # Create the email message
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
                margin-bottom: 15px;
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
                    {data.name}<br>
                    <a href="mailto:{data.email}" style="color: #004aad; text-decoration: none;">
                        {data.email}
                    </a>
                </div>
            
                <div class="label">Aihe</div>
                <div class="value" style="color: #004aad; font-weight: 500;">
                    {data.subject if data.subject else 'Ei aihetta'}
                </div>
            
                <div class="label">Viesti</div>
                <div class="message-content">
                    {data.message}
                </div>
            </div>
        
            <div style="text-align: center; color: #666; font-size: 0.9em; margin-top: 25px;">
                Tämä viesti lähetettiin Pohjosen Pajan kontaktilomakkeen kautta
            </div>
        </div>
        </body>
        </html>
        """
    msg = EmailMessage()
    msg['From'] = os.getenv('FROM_EMAIL')
    msg['To'] = os.getenv('TO_EMAIL')
    msg['Subject'] = data.subject
    msg.set_content(html_content, subtype='html')
    
    # Send the email
    try:
        with smtplib.SMTP(
            os.getenv('SMTP_SERVER', 'smtp.gmail.com'),
            int(os.getenv('SMTP_PORT', 587))
        ) as server:
            server.starttls()
            server.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASSWORD'))
            server.send_message(msg)
        return {"message": "Email sent successfully"}
    except Exception as e:
        print(f'SMTP error: {str(e)}')
        raise HTTPException(status_code=500, detail="Failed to send email")
    
    
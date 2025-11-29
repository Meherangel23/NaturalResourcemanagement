from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

router = APIRouter()

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    mobile: str
    message: str

@router.post("/contact/send-mail")
async def send_mail(form: ContactForm):
    # Configure your SMTP server details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"      # Replace with your password
    receiver_email = "info@nrms.co.in"    # Where you want to receive contact mails

    subject = f"Contact Form Submission from {form.name}"
    body = f"Name: {form.name}\nEmail: {form.email}\nMobile: {form.mobile}\nMessage: {form.message}"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return {"success": True, "message": "Mail sent successfully."}
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"success": False, "message": str(e)})

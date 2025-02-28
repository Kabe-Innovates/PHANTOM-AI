# email_sender/email_sender.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD

def send_email(recipient_email, subject, body):
    """Send the email with the given subject and body."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = 'kandanthulasi@gmail.com'  # The recipient email will be passed here
    msg['Subject'] = subject     # The subject will be passed here
    msg.attach(MIMEText(body, 'plain'))
    
    # Sending email using SMTP
    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Use TLS for security
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            text = msg.as_string()
            server.sendmail(EMAIL_USER, 'kandanthulasi@gmail.com', text)
            print(f"Email sent successfully to {recipient_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

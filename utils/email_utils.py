import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

def send_email_code(receiver_email: str, code: str):
    subject = "Movie Booking - Ваш код подтверждения"
    body = f"Здравствуйте!\n\nВаш код подтверждения: {code}\n\nСпасибо за использование нашего сервиса!"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  
            server.send_message(msg)  

        print(f"📬 Код успешно отправлен на {receiver_email}")
    except Exception as e:
        print("❌ Ошибка при отправке письма:", e)


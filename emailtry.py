import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from a .env file if using dotenv
load_dotenv()

def send_simple_email(recipient_email, subject, body):
    # Load email credentials from environment variables
    email_user = 'advaykajaria@gmail.com'
    email_pass = 'Advay@233'

    if not email_user or not email_pass:
        print("Email credentials not found. Please set them as environment variables.")
        return

    # Set up the email
    msg = MIMEText(body)
    msg['From'] = email_user
    msg['To'] = recipient_email
    msg['Subject'] = subject

    try:
        # Connect to the email server
        server = smtplib.SMTP('advaykajaria@gmail.com', 587)  # Replace 'smtp.gmail.com' with your email provider's SMTP server
        server.starttls()  # Secure the connection
        server.login(email_user, email_pass)  # Log in to the email server
        server.sendmail(email_user, recipient_email, msg.as_string())  # Send the email
        server.quit()  # Close the connection

        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    # Define recipient email, subject, and body of the email
    recipient_email = "kajaria.amritanshu@gmail.com"  # Replace with the recipient's email address
    subject = "Hello from Python"
    body = "This is a simple text message sent using Python."

    # Send the email
    send_simple_email(recipient_email, subject, body)

if __name__ == "__main__":
    main()

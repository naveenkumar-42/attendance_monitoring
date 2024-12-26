import smtplib
from email.mime.text import MIMEText

# Replace with your credentials
sender_email = 'fixit60656@gmail.com'
receiver_email = 'sabarish.it22@bitsathy.ac.in'
sender_password = 'rivflfrfcpkitmlc'

msg = MIMEText("Test email body")
msg['Subject'] = "Test Email"
msg['From'] = sender_email
msg['To'] = receiver_email

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print("Email sent successfully")
except Exception as e:
    print(f"Error: {e}")

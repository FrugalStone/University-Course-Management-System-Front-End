import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the SMTP server
    smtp_server = 'smtp.office365.com'
    smtp_port = 587

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to your Outlook account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(msg)
        print('Email sent successfully!')

    except Exception as e:
        print('An error occurred while sending the email:', str(e))

    finally:
        # Close the connection to the SMTP server
        server.quit()

# Get user input
sender_email = "elementreset@outlook.com"
sender_password = "Vinayak is the goat"
recipient_email = "mailvizzard@gmail.com"
subject = "Request for password reset"
message = "na team ku work chei ra pooka (sent through python 3 mail program. we did it guys. we finally did it. i am very proud of myself.)\nPS: Vaibav <3 you"

# Send the email
send_email(sender_email, sender_password, recipient_email, subject, message)

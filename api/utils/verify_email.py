from config import config
from cryptography.fernet import Fernet
import base64
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

cipher = Fernet(config["f-crypto-key"])


def send_email(email):
    """
    This function sends a verification email to the user.
    """

    # Encrypt the email
    encrypted_email = cipher.encrypt(email.encode())

    # Encode the encrypted data using Base64
    encoded_email = base64.urlsafe_b64encode(encrypted_email).decode()

    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Maverick-Habesha</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{
            background-color: #f9fafb;
            font-family: 'Roboto', sans-serif;
            font-size: 16px;
            line-height: 1.6;
            color: #333;
        }}

        h1 {{
            font-size: 36px;
            font-weight: 700;
            color: #333;
            margin-top: 40px;
            margin-bottom: 20px;
            text-align: center;
        }}

        p {{
            font-size: 18px;
            font-weight: 400;
            color: #666;
            margin-bottom: 30px;
            text-align: center;
        }}

        .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 50px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }}

        .button {{
            display: inline-block;
            margin-top: 40px;
            padding: 12px 40px;
            background-color: #337ab7;
            color: #fff;
            font-size: 18px;
            font-weight: 400;
            text-decoration: none;
            border-radius: 4px;
            transition: background-color 0.2s ease-in-out;
        }}

        .button:hover {{
            background-color: #23527c;
        }}

        @media (max-width: 767px) {{
            h1 {{
                font-size: 32px;
                margin-top: 20px;
                margin-bottom: 10px;
            }}

            p {{
                font-size: 16px;
                margin-bottom: 20px;
            }}

            .container {{
                padding: 30px;
            }}

            .button {{
                margin-top: 30px;
                padding: 12px 24px;
                font-size: 16px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Maverick-Habesha!</h1>
        <p>Thank you for joining our platform. To get started, please verify your email address.</p>
        <p class="center"> 
            <a class="button" href="http://localhost:5000/api/verify-email?token={encoded_email}">Verify Email</a>
        </p>
    </div>
</body>
</html>
"""

    text = f"""
    Welcome to Maverick-Habesha!
    """
    sender_email = config["email-name"]
    receiver_email = email
    password = config["email-password"]

    message = MIMEMultipart("alternative")
    message["Subject"] = "Please verify your email"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    return None


def verify_email_token(token):
    """This function verifies the email token."""

    # Decode the Base64 encoded data
    decoded_email = base64.urlsafe_b64decode(token)

    # Decrypt the email
    decrypted_email = cipher.decrypt(decoded_email).decode()

    return decrypted_email


def send_password_reset_email(email):
    """
    This function sends a password reset email to the user.
    """

    # Encrypt the email
    encrypted_email = cipher.encrypt(email.encode())

    # Encode the encrypted data using Base64
    encoded_email = base64.urlsafe_b64encode(encrypted_email).decode()

    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Reset your password</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{
            background-color: #f9fafb;
            font-family: 'Roboto', sans-serif;
            font-size: 16px;
            line-height: 1.6;
            color: #333;
        }}

        h1 {{
            font-size: 36px;
            font-weight: 700;
            color: #333;
            margin-top: 40px;
            margin-bottom: 20px;
            text-align: center;
        }}

        p {{
            font-size: 18px;
            font-weight: 400;
            color: #666;
            margin-bottom: 30px;
            text-align: center;
        }}

        .container {{
        
            max-width: 600px;
            margin: 0 auto;
            padding: 50px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }}

        .button {{
            display: inline-block;
            margin-top: 40px;
            padding: 12px 40px;
            background-color: #337ab7;
            color: #fff;
            font-size: 18px;
            font-weight: 400;
            text-decoration: none;
            border-radius: 4px;
            transition: background-color 0.2s ease-in-out;
        }}

        .button:hover {{
            background-color: #23527c;
        }}

        @media (max-width: 767px) {{
            h1 {{
                font-size: 32px;
                margin-top: 20px;
                margin-bottom: 10px;
            }}  

            p {{
                font-size: 16px;
                margin-bottom: 20px;
            }}

            .container {{
            
                padding: 30px;
            }}  

            .button {{
                margin-top: 30px;
                padding: 12px 24px;
                font-size: 16px;
            }}

        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Reset your password</h1>
        <p>Click the button below to reset your password.</p>
        <p class="center">
            <a class="button" href="http://localhost:5000/api/reset-password?token={encoded_email}">Reset Password</a>
        </p>
    </div>
</body>
</html>
"""

    text = f"""
    Reset your password
    """

    sender_email = config["email-name"]
    receiver_email = email
    password = config["email-password"]

    message = MIMEMultipart("alternative")
    message["Subject"] = "Reset your password"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    return None


def reset_password_token(token):
    """This function verifies the reset password token."""

    # Decode the Base64 encoded data
    decoded_email = base64.urlsafe_b64decode(token)

    # Decrypt the email
    decrypted_email = cipher.decrypt(decoded_email).decode()

    return decrypted_email

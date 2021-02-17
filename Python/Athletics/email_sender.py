import smtplib
import ssl
import getpass

sender_email = "arctic1878.programming@gmail.com"
receiver_email = "martin.stensen92@gmail.com"
message = """Subject: This is a test

This is a test message sent from Python.
"""
# a = 0
# b = 9
# message = f'Subject: f string test\n\na = {a}, b = {b}'


def main():
    port = 465  # For SSL
    password = getpass.getpass("Type your password and press enter: ")

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


if __name__ == "__main__":
    main()

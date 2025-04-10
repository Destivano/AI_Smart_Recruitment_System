import os
import imaplib
import email
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import googleapiclient.http
from google.auth.transport.requests import Request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
EMAIL_USER = "your_email@example.com"  # ⚠️ Attention : Ne pas partager cette adresse e-mail
EMAIL_PASS = "your_password_here"  # ⚠️ Attention : Ne pas partager ce mot de passe
MAILBOX = "INBOX"
SAVE_FOLDER = os.path.join(os.path.expanduser("~"), "Desktop", "CV AI")

# Assurer l'existence du dossier de stockage
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

# Connexion à Gmail
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL_USER, EMAIL_PASS)
mail.select(MAILBOX)

# Date 3 minutes avant maintenant au format IMAP
three_minutes_ago = (datetime.now() - timedelta(minutes=3)).strftime("%d-%b-%Y")

# Recherche des e-mails envoyés depuis 3 minutes avec sujet "Scheduled Job Interview"
status, messages = mail.search(None, f'(SINCE {three_minutes_ago} SUBJECT "Scheduled job interview")')
email_ids = messages[0].split()

# Fonction pour envoyer un e-mail de relance
def send_follow_up_email(to_email):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = to_email
    msg['Subject'] = "Follow-up: Scheduled Job Interview"

    body = "Dear Candidate,\n\nWe noticed that you have not responded to our email about the scheduled job interview. Please let us know your availability.\n\nBest regards,\nYour Company"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    text = msg.as_string()
    server.sendmail(EMAIL_USER, to_email, text)
    server.quit()

# Vérifier les réponses aux e-mails de "Scheduled Job Interview"
for email_id in email_ids:
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            from_email = email.utils.parseaddr(msg['To'])[1]

            # Rec
            # herche des e-mails envoyés par le candidat après avoir reçu l'e-mail de "Scheduled Job Interview"
            status, response_messages = mail.search(None, f'(SINCE "{(datetime.now()).strftime("%d-%b-%Y")}" FROM "{from_email}")')
            print(from_email)
            response_email_ids = response_messages[0].split()

            # Si aucune réponse n'est trouvée, envoyer un e-mail de relance
            if not response_email_ids:
                send_follow_up_email(from_email)
                print(f"📧 Relance envoyée à : {from_email}")

# Déconnexion
mail.logout()

print("✅ Relance envoyée à tous les candidats n'ayant pas répondu !")

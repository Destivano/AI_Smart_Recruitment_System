import os
from email.message import EmailMessage
import ssl
import smtplib
import re




cv_json = {"cv": "Name: candidate name, email: candidate.email@example.com,"} # Replace with the actual CV JSON data

# Extract the email from cv_json with regular expressions
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
match = re.search(email_pattern, cv_json["cv"])

if match:
    extracted_email = match.group(0)
    print(f"Extracted Email: {extracted_email}")
else:
    print("No email found in the CV.")




email_sender = 'your.email@example.com'  # Replace with your email address
email_password = 'your_password'  # Replace with your email password
email_receiver = extracted_email

candidate_name = "John Doe"
job_title = "Software Engineer"
company_name = "Tech Corp"
interview_date = "2023-10-15"
interview_time = "10:00 AM"
time_zone = "PST"
location = "123 Tech Street, Tech City"  # or "https://videocall.link"
estimated_duration = "1 hour"
interview_format = "In-person"
interviewers = "Jane Smith (HR Manager)"
confirmation_deadline = "2023-10-10"
your_name = "your name"  # Replace with your name
your_job_title = "your job title"
contact_information = "your.email@example.com"

body = f"""Dear {candidate_name},

We are pleased to inform you that you have been selected for an interview for the {job_title} position at {company_name}. We were impressed with your application and would love to learn more about your skills and experience.

**Interview Details:**
- **Date:** {interview_date}
- **Time:** {interview_time} ({time_zone})
- **Location:** {location}
- **Duration:** {estimated_duration}
- **Interview Format:** {interview_format}
- **Interviewer(s):** {interviewers}

Please confirm your availability by replying to this email by {confirmation_deadline}. If you have any questions or need to reschedule, feel free to let us know.

We look forward to speaking with you soon!

Best regards,
{your_name}
{your_job_title}
{company_name}
{contact_information}
"""

subject = f"Invitation to Interview {job_title} Position at {company_name}"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())



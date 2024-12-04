import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox
import json

# Load environment variables
load_dotenv()

# SMTP configuration
SMTP_SERVER = 'smtp.mail.yahoo.com'
SMTP_PORT = 587
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
RESUME_FILE = 'Resume.pdf'
EMAIL_TEMPLATE_FILE = 'email_template.txt'
SUBJECT = "Excited to Connect – Frist Name-Last Name DevOps Application"

# Path to track sent emails
SENT_EMAILS_FILE = 'sent_emails.json'

def read_file(file_path):
    """Safely read the content of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

def extract_name_from_email(email):
    """Extract recipient's first and last name from the email."""
    try:
        # Remove domain part and split the first and last name
        local_part = email.split('@')[0]
        name_parts = local_part.split('.')
        if len(name_parts) >= 2:
            return f"{name_parts[0].capitalize()} {name_parts[1].capitalize()}"
        else:
            return name_parts[0].capitalize()
    except Exception as e:
        print(f"Error extracting name from email: {e}")
        return None

def send_email(recipient, subject, body, resume_path, status_label, disable_widgets_func):
    """Send an email with an attachment."""
    try:
        # Disable all widgets while sending
        disable_widgets_func(True)
        status_label.config(text="Sending email... Please wait.", fg="blue")

        # Check if email has already been sent
        if email_sent(recipient):
            status_label.config(text=f"Email already sent to {recipient}.", fg="red")
            disable_widgets_func(False)
            return

        # Create the email
        msg = EmailMessage()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.set_content(body)

        # Attach resume
        with open(resume_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(resume_path)
            msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

        # Send the email via Yahoo or Gmail
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {recipient}")

        # Log this email as sent
        log_sent_email(recipient)

        # Update status to show success
        status_label.config(text=f"Email sent successfully to {recipient}.", fg="green")

    except FileNotFoundError:
        print(f"Error: Resume file '{resume_path}' not found.")
        status_label.config(text="Error: Resume file not found.", fg="red")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")
        status_label.config(text=f"Failed to send email: {e}", fg="red")
    finally:
        # Re-enable widgets after email is sent
        disable_widgets_func(False)

def email_sent(recipient_email):
    """Check if an email has already been sent to the recipient."""
    try:
        if os.path.exists(SENT_EMAILS_FILE):
            with open(SENT_EMAILS_FILE, 'r') as f:
                sent_emails = json.load(f)
            return recipient_email in sent_emails
        return False
    except Exception as e:
        print(f"Error checking sent emails: {e}")
        return False

def log_sent_email(recipient_email):
    """Log an email as sent."""
    try:
        if os.path.exists(SENT_EMAILS_FILE):
            with open(SENT_EMAILS_FILE, 'r') as f:
                sent_emails = json.load(f)
        else:
            sent_emails = []

        sent_emails.append(recipient_email)

        with open(SENT_EMAILS_FILE, 'w') as f:
            json.dump(sent_emails, f)
    except Exception as e:
        print(f"Error logging sent email: {e}")

def send_button_click(status_label, disable_widgets_func):
    """Handle the send button click."""
    recipient_email = email_entry.get()

    if not recipient_email:
        messagebox.showerror("Error", "Please provide the recipient's email")
        return

    # If auto-naming is selected, extract the name from the email
    if auto_name_var.get():
        recipient_name = extract_name_from_email(recipient_email)
        if not recipient_name:
            messagebox.showerror("Error", "Failed to extract name from email")
            return
    else:
        # Use the selected team name if auto-name is not checked
        recipient_name = team_var.get()

    if not recipient_name:
        messagebox.showerror("Error", "Please provide the recipient's name")
        return

    # Read the email template
    email_body_template = read_file(EMAIL_TEMPLATE_FILE)
    if email_body_template is None:
        messagebox.showerror("Error", "Email template not found.")
        return

    # Personalize the email body
    email_body = email_body_template.replace("[Recipient's Name or Team]", recipient_name)

    # Send the email
    send_email(recipient_email, SUBJECT, email_body, RESUME_FILE, status_label, disable_widgets_func)

def disable_widgets(disable):
    """Enable or disable widgets."""
    email_entry.config(state="disabled" if disable else "normal")
    name_entry.config(state="disabled" if disable else "normal")
    send_button.config(state="disabled" if disable else "normal")
    team_dropdown.config(state="disabled" if disable else "normal")

# Set up the GUI
root = tk.Tk()
root.title("Cold Email Sender")
root.geometry("400x350")

# Email Label
email_label = tk.Label(root, text="Recipient's Email:")
email_label.pack(pady=5)
email_entry = tk.Entry(root, width=40)
email_entry.pack(pady=5)

# Recipient Team Dropdown (Default options: HR Team, Talent Acquisition Team)
team_label = tk.Label(root, text="Select Team:")
team_label.pack(pady=5)
team_var = tk.StringVar(value="HR Team")  # Default value
team_dropdown = tk.OptionMenu(root, team_var, "HR Team", "Talent Acquisition Team")
team_dropdown.pack(pady=5)

# Name Label
name_label = tk.Label(root, text="Recipient's Name (Optional):")
name_label.pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

# Auto-name checkbox
auto_name_var = tk.BooleanVar()
auto_name_checkbox = tk.Checkbutton(root, text="Auto-name from email address", variable=auto_name_var)
auto_name_checkbox.pack(pady=5)

# Status Label for displaying email send status
status_label = tk.Label(root, text="", fg="black")
status_label.pack(pady=10)

# Send Button
send_button = tk.Button(root, text="Send Email", command=lambda: send_button_click(status_label, disable_widgets))
send_button.pack(pady=20)

# Run the GUI
root.mainloop()

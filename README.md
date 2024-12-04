# Cold Email Sender

A simple Python tool to help you automate sending cold emails to recruiters. Just enter the recipient's details, and the email will be sent with your resume attached. It supports both **Yahoo** and **Gmail** SMTP servers, making it a versatile tool for your job search.

### 🚀 Features:
- **Personalized Emails**: Easily customize the recipient's name and email.
- **Resume Attachment**: Automatically attach your resume with each email.
- **Customizable Email Template**: Modify the email text to reflect your unique style.
- **Supports Yahoo & Gmail**: Seamlessly switch between Gmail or Yahoo SMTP servers.

---

## 📂 Project Directory Structure

Here’s a glance at how the project is structured:

```
cold-email-sender/
│
├── .env                  # Contains sensitive data like email and app password
├── cold-email.py         # The main Python script
├── email_template.txt    # The cold email template text file
├── resume.pdf            # Your resume (make sure it's in the same folder as the script)
├── requirements.txt      # Python dependencies (python-dotenv and secure-smtplib)
└── README.md             # Project documentation
```

### 📄 File Descriptions:
- **`.env`**: Stores sensitive information such as your email and app password.
- **`cold-email.py`**: The core script responsible for sending the cold emails.
- **`email_template.txt`**: The customizable email template.
- **`resume.pdf`**: Your resume, which will be attached automatically to each email.
- **`requirements.txt`**: The list of dependencies required for the script (such as `python-dotenv` and `secure-smtplib`).
- **`README.md`**: This documentation file you're reading.

---

## 🛠️ Setup Instructions

### 1. Clone the repository:

```bash
git clone https://github.com/syedimran18/cold-email-sender.git
cd cold-email-sender
```

### 2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure your `.env` file:

Create and edit your `.env` file with your email and app password:

```env
SENDER_EMAIL=your_email@example.com
SENDER_PASSWORD=your_app_password
```

#### 🔑 **How to Get App Passwords**:

- **Yahoo Mail**:
  1. Go to [Yahoo Account Security](https://login.yahoo.com/account/security).
  2. Enable **2-Step Verification** and generate an **app password**.
  3. Add the app password to your `.env` file.

- **Gmail**:
  1. Go to [Google Account Security](https://myaccount.google.com/security).
  2. Enable **2-Step Verification** and generate an **app password**.
  3. Add it to your `.env` file.

### 4. Edit your email template:

Customize the `email_template.txt` to reflect your message. Example:

```text
Dear [Recipient's Name],

My Nmae is Mr. Blah blam. I have Blah blah... yapping 🗣️ blah blah blah

I’ve attached my resume for your reference.

Thanks for your time!
```

### 5. Run the script:

Execute the script using the following command:

```bash
python cold-email.py
```

### 6. Sending Emails:

- You'll be prompted to enter the recipient's email and name.
- After entering the details, hit **Send Email** to send the email along with your resume.

### 7. Switching Between Gmail and Yahoo SMTP:

You can switch between Gmail and Yahoo SMTP servers by modifying the `cold-email.py` file:

```python
# Yahoo SMTP settings
SMTP_SERVER = 'smtp.mail.yahoo.com'

# Gmail SMTP settings
# SMTP_SERVER = 'smtp.gmail.com'
```

---

## ⚠️ Troubleshooting:

- **Connection error**: Ensure your internet connection is stable and verify that you are using the correct SMTP settings for your provider.
- **File not found**: Ensure `resume.pdf` and `email_template.txt` are in the same directory as the script.

---

## 📝 License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 👏 Credits

**Idea and Concept by [Syed Imran](https://github.com/syedimran18)**, executed with the help of **OpenAI (ChatGPT)**. A little creativity and technology go a long way!

[![GitHub](https://img.shields.io/badge/GitHub-syedimran18-blue?logo=github&logoColor=white)](https://github.com/syedimran18)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Syed_Imran-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/syed-imran18/)

---

### 🌟 Let's Connect!

If you have any questions or feedback, feel free to reach out. Happy emailing!

---

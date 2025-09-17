import time
import json
import smtplib
from datetime import datetime

# Paths
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # Windows
# hosts_path = "/etc/hosts"  # Linux / Mac
redirect = "127.0.0.1"

# Load sites
with open("blocked_sites.txt") as file:
    websites = [line.strip() for line in file if line.strip()]

# Load config
with open("config.json") as f:
    config = json.load(f)

start_hour = config["start_hour"]
end_hour = config["end_hour"]
email_notifications = config["email_notifications"]
email_sender = config["email_sender"]
email_password = config["email_password"]
email_receiver = config["email_receiver"]

def send_email_notification():
    """Send email when blocking starts"""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, email_password)
        subject = "Website Blocker Active"
        body = f"Website Blocker activated at {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(email_sender, email_receiver, message)
        server.quit()
        print("[INFO] Email notification sent.")
    except Exception as e:
        print("[ERROR] Email notification failed:", e)

def block_websites():
    """Block listed websites by modifying hosts file"""
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for site in websites:
            if site not in content:
                file.write(f"{redirect} {site}\n")

def unblock_websites():
    """Unblock websites by cleaning hosts file"""
    with open(hosts_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(site in line for site in websites):
                file.write(line)
        file.truncate()

print("[INFO] Website Blocker running. Press CTRL+C to stop.")

email_sent = False

while True:
    now = datetime.now()
    if start_hour <= now.hour < end_hour:
        block_websites()
        if email_notifications and not email_sent:
            send_email_notification()
            email_sent = True
        print(f"[{now.strftime('%H:%M')}] Blocking active.")
    else:
        unblock_websites()
        email_sent = False
        print(f"[{now.strftime('%H:%M')}] Blocking inactive.")
    time.sleep(60)  # check every 1 minute

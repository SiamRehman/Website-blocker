# Website Blocker

A simple Python tool to block distracting websites during specific hours.  
It also optionally sends an email notification when the block is active.

## Features
- Time-based website blocking
- Configurable list of websites
- Optional email notification when blocking starts
- Works on Windows, Linux, and macOS (requires admin privileges)

## How It Works
The script edits your computer's `hosts` file to redirect blocked websites to `127.0.0.1`.  
During allowed hours, it restores access.

## Setup
1. Clone this repo.
2. Add the websites you want to block in `blocked_sites.txt`.
3. Configure `config.json`:
   - `start_hour` and `end_hour` for blocking hours (24-hour format).
   - Set `"email_notifications": true` and fill in your email credentials if you want alerts.
4. Run the script with admin privileges:
   ```bash
   python website_blocker.py
   ```

## Notes
- Admin privileges are required to modify the hosts file.
- For Linux/macOS use `/etc/hosts` as the `hosts_path`.
- Use an app password for Gmail if 2FA is enabled.

# IMAP Email Deletion Script

## Overview
This Python script facilitates the deletion of emails from specified folders on an IMAP server, specifically tailored for Gmail. It connects to the IMAP server, scans through folders (excluding the `[Gmail]` mailbox), and allows users to delete emails from a particular sender based on their email address.

## Requirements
- Python 3.x
- `imapclient` library (install via `pip install imapclient`)

## Usage
1. **Configuration**:
   - Replace `'yourz@email.com'` with your Gmail address.
   - Replace `'apps password'` with the app password generated for your Gmail account. If you haven't generated an app password, you can follow [Google's instructions](https://support.google.com/accounts/answer/185833?hl=en) to do so.

2. **Running the Script**:
   - Execute the script using the command `python imap_email_deletion.py`.

Upon execution, the script will perform the following actions:
- Connect to the Gmail IMAP server.
- List all folders excluding the `[Gmail]` mailbox.
- Iterate through each folder and search for emails from a specified target email address (`'targetemail.com'`).
- Prompt the user to confirm the deletion of found emails.
- Permanently delete the selected emails.

## Important Notes
- **Email Deletion**: This script permanently deletes emails from the specified folders. Exercise caution while using it, as there is no way to recover deleted emails.
- **Gmail Authentication**: Ensure that you use an app password generated for your Gmail account to authenticate the script. Regular account passwords may not work due to Gmail's security policies.
- **Target Email Address**: Adjust the target email address (`'targetemail.com'`) in the script to match the sender's email address you wish to delete emails from.

## How to Run
```bash
python imap_email_deletion.py
```

## Author
Priyanka Zala

## License
This project is licensed under the [MIT License](LICENSE).
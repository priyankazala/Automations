# Email Reader Script

## Overview

This Python script allows you to access an email account via IMAP, fetch the top `N` emails from the inbox, and process them. It retrieves email subjects, senders, and content, including attachments and HTML emails.

## Prerequisites

Before using this script, ensure you have:

- Python installed on your system (version 3.x recommended).
- Access to an email account with IMAP enabled.
- Generated an app-specific password if using Gmail or a similar service.

## Setup

1. Clone or download the repository containing the script.

2. Open the script `email_reader.py` in a text editor.

3. Replace the placeholder values with your email credentials:
   - `username`: Your email address.
   - `password`: Your app-specific password generated for accessing email via IMAP.
   - `imap_server`: The IMAP server address of your email provider.

4. Save the changes to the script.

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory containing the script.

3. Run the script by executing the following command:
   ```
   python email_reader.py
   ```

4. The script will connect to your email account, fetch the top `N` emails from the inbox, and process them.

5. Follow the instructions printed in the terminal for further actions, such as viewing email content or attachments.

## Customization

- You can customize the number of top emails to fetch (`N`) by modifying the value in the script.
- Additionally, you can customize the behavior of the script, such as saving attachments to a specific directory or modifying the folder structure for saving emails.

## Dependencies

- This script relies on the `imaplib`, `email`, `email.header`, `webbrowser`, and `os` modules, which are part of Python's standard library.

## Support

If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
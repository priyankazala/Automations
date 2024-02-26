from imapclient import IMAPClient

# Connect to the IMAP server
def delete_messages(target_email):
    with IMAPClient('imap.gmail.com') as client:
        client.login('your@email.com', 'apps password')
        try:
            # Get a list of all folders
            folders = client.list_folders()

            # Iterate through each folder
            for folder_info in folders:
                folder_name = folder_info[-1]  # Get the name of the folder
                if folder_name == '[Gmail]':
                    continue  # Skip the [Gmail] mailbox
                print(f"Processing folder: {folder_name}")
            
                # Select the current folder
                client.select_folder(folder_name)

                # Search for emails from the target email address
                messages = client.search(['FROM', target_email])

                # Mark emails for deletion
                if messages:
                    print(len(messages),' emails found to be deleted:')

                    confirmation = input("Do you want to delete these emails? (yes/no): ").strip().lower()
                    if confirmation == 'yes' or 'y':
                        client.delete_messages(messages)
                        # Expunge (permanently delete) the emails marked for deletion
                        client.expunge(messages)

                        print("Emails deleted successfully.")
                    else:
                        print("You aborted the process.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

target_email  = input("Enter the email address whose mails you want to delete:")
delete_messages(target_email)
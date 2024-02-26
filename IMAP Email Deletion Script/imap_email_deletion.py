from imapclient import IMAPClient

# Connect to the IMAP server
with IMAPClient('imap.gmail.com') as client:
    client.login('yourz@email.com', 'apps password')
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
            messages = client.search(['FROM', 'targetemail.com'])

            # Mark emails for deletion
            if messages:
                print("Found the following emails to be deleted:")
                for msg_id in messages:
                    print(f"- Message ID: {msg_id}")
                
                confirmation = input("Do you want to delete these emails? (yes/no): ").strip().lower()
                if confirmation == 'yes':
                    client.delete_messages(messages)
                    # Expunge (permanently delete) the emails marked for deletion
                    client.expunge(messages)

                    print("Emails deleted successfully.")
                else:
                    print("Emails were not deleted.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Whatsapp-Gmail-Auto-Sender
A web application with a friendly UI that uses a CSV containing a phone number or email in the first column and the name of the person in the second column.

To start using the scripts firstly the user needs to select the CSV file in the bottom left area.
While writing the text content the user can use {name} whenever they want to use the personalized name.

The first button opens a frame that allows the user to check if the file has more than one user with the same phone number or email address.
The button "Changed" deletes all the duplicates but saves the first unique person with that phone number or email.
The "Undo" button reverts the changes.

The second button opens the What's App script.
The script works with What's App Web. 
After writing the message content, pressing the "Run" button will start the script.

The third button opens the Gmail script.
The script works with Gmail shortcuts enabled. 
The Subject and Message should never be empty. 
After writing the message content, pressing the "Run" button will start the script.


!!! To stop the script the fail-safe mode is moving the mouse to any corner of the screen.

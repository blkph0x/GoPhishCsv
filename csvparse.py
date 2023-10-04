import csv

# Create a dictionary to store the data
email_data = {}

# Read the CSV file
with open('your_file.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        email = row['email']
        status = row['status']

        # Initialize the email entry if not present
        if email not in email_data:
            email_data[email] = {
                'Email Opened': False,
                'Clicked Link': False,
                'Submitted Data': False
            }

        # Update the status value
        if status == 'Email Opened':
            email_data[email]['Email Opened'] = True
        elif status == 'Clicked Link':
            email_data[email]['Clicked Link'] = True

# Check for "Submitted Data" and set all statuses to True
with open('your_file.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        email = row['email']
        status = row['status']

        if status == 'Submitted Data':
            if email in email_data:
                email_data[email]['Email Opened'] = True
                email_data[email]['Clicked Link'] = True
                email_data[email]['Submitted Data'] = True

# Ensure that "Email Opened" is True if "Clicked Link" is True
for email, status_flags in email_data.items():
    if status_flags['Clicked Link']:
        status_flags['Email Opened'] = True

# Prepare the output data
output_data = []

# Write the header row
header = ['Email', 'Email Opened', 'Clicked Link', 'Submitted Data']
output_data.append(header)

# Generate the output rows for all emails
for email, status_flags in email_data.items():
    row = [email, status_flags['Email Opened'], status_flags['Clicked Link'], status_flags['Submitted Data']]
    output_data.append(row)

# Write the output to a new CSV file
with open('output.csv', mode='w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(output_data)

print("Extraction, formatting, and filtering complete. Output saved to 'output.csv'")

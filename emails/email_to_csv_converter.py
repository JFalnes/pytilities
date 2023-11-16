
# Open email.txt and read the emails
with open('email.txt', 'r') as email_file:
    # Read lines and filter out empty lines or lines with only whitespace
    emails = [line.strip() for line in email_file if line.strip()]

# Write the emails to GroupMembers.csv following the provided template
with open('GroupMembers.csv', 'w') as output_file:
    # Write the header
    output_file.write("version:v1.0\n")
    output_file.write("memberObjectIdOrUpn\n")
    # Write each email on a new line without any additional space
    output_file.writelines(email + '\n' for email in emails)

# Print a message indicating that the script has finished writing to the output file
print("Finished writing to GroupMembers.csv!")
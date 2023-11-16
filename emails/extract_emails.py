import re


def extract_emails(input_file, output_file):
    """
    Extracts all email addresses from a given input file and writes them to an output file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.

    Returns:
        None
    """
    # Open the input file and read its contents
    with open(input_file, 'r') as f:
        content = f.read()

    # Use regular expression to find all email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, content)

    # Open the output file and write the email addresses
    with open(output_file, 'w') as f:
        for email in emails:
            f.write(email + '\n')

if __name__ == '__main__':
    input_file = 'input.txt'  # Replace with your input file name
    output_file = 'emails.txt'  # Replace with your desired output file name
    extract_emails(input_file, output_file)

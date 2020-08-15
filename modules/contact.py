import csv
from datetime import date


html_escape_table = {
    '&': '&amp;',
    '"': '&quot;',
    '\'': '&apos;',
    '>': '&gt;',
    '<': '&lt;',
}


def html_escape(text):
    ''' Produce entities within text. '''
    return ''.join(html_escape_table.get(c, c) for c in text)


def write_to_file(data):
    with open('./Database/database.txt', mode='a') as database:
        today = date.today().strftime('%B %d, %Y - %H:%M:%S')
        email = html_escape(data['email'])
        subject = html_escape(data['subject'])
        message = html_escape(data['message'])
        database.write(f'\n{today}:\nFrom: {email}\nSubject: {subject}\nMessage: {message}\n----------------\n')


def write_contact_info(data):
    with open('./Database/database.csv', mode='a', newline='') as csvfile:
        today = date.today().strftime('%B %d, %Y%H:%M:%S')
        email = html_escape(data['email'])
        subject = html_escape(data['subject'])
        message = html_escape(data['message'])
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([today, email, subject, message])

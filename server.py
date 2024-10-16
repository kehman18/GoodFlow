'''necessary for the server to run properly'''
import csv
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

def send_mail_service(name, email, service, service_date, special_request):
    '''the function helps send mail'''
    msg = Message(
        subject='A new message from {email}',
        sender='adekolaolabisi7@gmail.com',
        recipients=['adekolaolabisi7@gmail.com'],)

        # Form a single sentence for the email body
    msg.body = f"Sender's Name: {name}\n\n Sender's Mail: ({email})\n\n {name} has reached out with the following details. They are requesting the service {service} on {service_date}. Special request: {special_request}."
    mail.send(msg)

def send_mail_contact(name, email, subject, message):
    '''the function helps send mail'''
    msg = Message(
        subject='A new message from {email}',
        sender='adekolaolabisi7@gmail.com',
        recipients=['adekolaolabisi7@gmail.com'],)

        # Form a single sentence for the email body
    msg.body = f"Sender's Name: {name}\n\n Sender's Mail: ({email})\n\n {name} has reached out with the following message details. Subject: {subject}, Message: {message}."
    mail.send(msg)
    
# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'adekolaolabisi7@gmail.com'
app.config['MAIL_PASSWORD'] = 'rlehmineppqafgpz'

mail = Mail(app)

# Route for the home page
@app.route('/')
def home_page():
    '''renders the home page'''
    return render_template('index.html')

# Route for the contact page
@app.route('/contact')
def contact():
    '''this function receives the data from the contact form'''
    return render_template('contact.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    '''this funtion is to run the submit the action on contact.html'''
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        send_mail_contact(name, email, subject, message)

        with open('contact.database.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([name, email, subject, message])


        return redirect('thankyou.html')

@app.route('/service-request', methods=['POST'])
def service_request():
    '''this function helps handle the service request'''
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        service = request.form['service']
        service_date = request.form['service_date']
        special_request = request.form['special_request']

        send_mail_service(name, email, service, service_date, special_request)

        with open('service_database.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([name, email, service, service_date, special_request])

        return redirect('thankyou.html')


# Dynamic route for other HTML pages
@app.route('/<string:page_name>')
def html_page(page_name):
    '''This page is to display the html page'''
    return render_template(page_name)

#Route to handle a 404 error
@app.errorhandler(404)
def page_not_found(e):
    '''this function handles the page not found error'''
    return render_template('not-found.html'), 404

#first start with splitting the database to the service database.
#send different Messages based on the form filled by the end user
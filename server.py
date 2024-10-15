'''necessary for the server to run properly'''
import csv
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

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

        subject = request.form.get('subject' 'NULL')
        message = request.form.get('message' 'NULL')
        service = request.form.get('service' 'NULL')
        service_date = request.form.get('service_date', 'NULL')
        special_request = request.form.get('special_request', 'NULL')

        with open('database.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([name, email, subject, message, service, service_date, special_request])
        
        return redirect('thankyou.html')

        def send_mail()
            msg = Message(
                subject='A new message from {email}',
                sender='adekolaolabisi7@gmail.com',
                recipients=['adekolaolabisi7@gmail.com'],)
            msg.body = f'Subject: {subject}\n\nFrom: {message}\n\nMessage: {message}\n\nService: {service}'
            msg.send(msg)

# Dynamic route for other HTML pages
@app.route('/<string:page_name>')
def html_page(page_name):
    '''This page is to display the html page'''
    return render_template(page_name)

#Route to handle a 404 error
@app.errorhandler(404)
def page_not_found(e):
    # this function handles the page not found error
    return render_template('not-found.html'), 404

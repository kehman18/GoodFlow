'''necessary for the server to run properly'''
from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home_page():
    return render_template('index.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Dynamic route for other HTML pages
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

#Route to handle a 404 error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('not-found.html'), 404

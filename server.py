'''this are all the modules needed to get things done'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    '''this is the function to the home page'''
    return render_template('index.html')
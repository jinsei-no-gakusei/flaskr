# all the imports
#from __future__ import with_statement
from contextlib import closing
#import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort,render_template,flash
import os

print 'doing this thing from'

# configuration
DEBUG = True
SECRET_KEY = 'mokoronkwo'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.before_request
def appbefore():
	if not request.host == 'martin.okoronkwo.me':
		return redirect('http://martin.okoronkwo.me',code = 301)
		 


@app.route('/')
def index():
    return render_template('indexone.html')
	
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 80))
	app.run(host='0.0.0.0', port=port)

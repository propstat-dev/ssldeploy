from flask import render_template
from ssldeploy import ssldeploy

@ssldeploy.route('/')
@ssldeploy.route('/index')
def index():
    brand = {'brandname' : 'company'}
    return render_template('index.html', title='SSL Deploy Admin Log-In', brand=brand)
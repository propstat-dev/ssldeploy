from flask import render_template
from ssldeploy import ssldeploy

@ssldeploy.route('/')
@ssldeploy.route('/index')
def index():
    brand = {'brandname' : 'companyname'}
    return render_template('selfservice/userlogin.html', title='SSL Deploy Self Service', brand=brand)

@ssldeploy.route('/admin/')
def admin():
    brand = {'brandname' : 'companyname'}
    return render_template('admin/adminlogin.html', title='SSL Deploy Admin Interface', brand=brand)
from flask import render_template, flash, redirect
from ssldeploy import ssldeploy
from ssldeploy.forms import UserLoginForm

@ssldeploy.route('/')
@ssldeploy.route('/index')
def index():
    brand = {'brandname' : 'companyname'}
    form = UserLoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.user_login_email.data, form.user_login_rememberme.data))
        return redirect('/admin/')
    return render_template('selfservice/userlogin.html', title='SSL Deploy Self Service', brand=brand, form=form)

@ssldeploy.route('/admin/')
def admin():
    brand = {'brandname' : 'companyname'}
    return render_template('admin/adminlogin.html', title='SSL Deploy Admin Interface', brand=brand)
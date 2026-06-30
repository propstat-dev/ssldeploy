from flask import render_template, flash, redirect
from ssldeploy import ssldeploy
from ssldeploy.forms import AdminLoginForm, UserLoginForm

@ssldeploy.route('/', methods=['GET', 'POST'])
def index():
    brand = {'brandname' : 'companyname'}
    form = UserLoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.user_login_username.data, form.user_login_rememberme.data))
        return redirect('/admin/')
    return render_template('selfservice/userlogin.html', title='SSL Deploy Self Service', brand=brand, form=form)

@ssldeploy.route('/admin/', methods=['GET', 'POST'])
def admin():
    brand = {'brandname' : 'companyname'}
    form = AdminLoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.admin_login_username.data, form.admin_login_rememberme.data))
        return redirect('/')
    return render_template('admin/adminlogin.html', title='SSL Deploy Admin Interface', brand=brand, form=form)

@ssldeploy.route('/admin/dashboard/')
def admin_dashboard():
    return render_template('admin/admin-dashboard.html', title='SSL Deploy Admin Dashboard')
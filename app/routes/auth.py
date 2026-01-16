from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

USER = {
    "username": "admin",
    "password": "admin"
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USER['username'] and request.form['password'] == USER['password']:
            session['user'] = USER['username']
            return redirect(url_for('tasks.view_tasks'))
        flash("Invalid login", "danger")
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))

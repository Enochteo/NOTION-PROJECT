from flask import Blueprint,render_template,request,flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash


auth =  Blueprint('auth',__name__, template_folder='__templates')

@auth.route('/login',methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.',category = 'error')
        else:
            new_User =  User(email=email,firstName=firstName,password=generate_password_hash(password1,method='sha256'))
            db.session
            flash('Account created successfully!',category = 'success')

    return render_template("sign.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/ask_ai')
def ask_ai():
    return render_template("ask_ai.html")

@auth.route('/time_management')
def time_management():
    return render_template("timemgmnt.html")

@auth.route('/task_management')
def task_management():
    return render_template("task.management.html")
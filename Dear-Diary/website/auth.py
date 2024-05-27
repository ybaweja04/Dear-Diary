from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__, template_folder='./template')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        Password = request.form.get('Password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.Password, Password):
                flash('LOGGED IN SUCCESSFULLY :)', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('INCORRECT PASSWORD :(', category='NA')
        else:
            flash('EMAIL DOES NOT EXIST :(', category='NA')
            
    return render_template('login.html', user=current_user)

    
    
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/SignUp', methods=['GET', 'POST'])
def SignUp():
    if request.method == 'POST':
        email = request.form.get('email')
        Username = request.form.get('Username')
        Password0 = request.form.get('Password0')
        Password1 = request.form.get('Password1')
    
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='NA')
        elif len(email) < 5:
            flash('Email must be greater than 5 characters.', category='NA')
        elif len(Username) < 2:
            flash('Username must be greater than 2 characters.', category='NA')
        elif len(Password0) < 8:
            flash('Password must be at least 8 characters.', category='NA')
        elif Password0 != Password1:
            flash('Confirmation password does not match the original password.', category='NA')
        else:
            new_user = User(email=email, Username=Username, Password=generate_password_hash(Password0, method='pbkdf2:sha256'))

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('ACCOUNT CREATED :) ', category='success')
            return redirect(url_for('views.home'))

    return render_template('SignUp.html', user=current_user)


    return render_template('SignUp.html', user=current_user)
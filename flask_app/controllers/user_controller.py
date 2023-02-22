from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user_model import User
from flask_app.models.vehicle_model import Vehicle

@app.route('/')
def user():
    return render_template('registration.html')

@app.route('/register', methods=['post'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'cin': request.form['cin'],
        'password':bcrypt.generate_password_hash(request.form['password'])
    }
    user=User.register(data)
    session['user_id']=user

    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')
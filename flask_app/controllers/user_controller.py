from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user_model import User
from flask_app.models.vehicle_model import Vehicle
# ============= display route =============
@app.route('/')
def user():
    return render_template('registration.html')
# ============= action route =============
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

    return redirect('/')
# ============= display route =============
@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/')
    user= User.get_by_id({'id': session['user_id']})
    return render_template("home.html",user=user)
# ============= action route =============
@app.route('/login', methods=['POST'])
def login():
    user_from_db = User.get_by_email(request.form)
    if not user_from_db:
        flash("invalid Email / Password", "email")
        return redirect('/')
    if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        flash("Invalid Email / Password", "password")
        return redirect('/')
    session['user_id'] = user_from_db.id
    return redirect('/home')
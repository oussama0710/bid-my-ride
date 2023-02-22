from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user_model import User
from flask_app.models.vehicle_model import Vehicle

@app.route('/add', methods=['post'])
def add_product():
    vehicle_data={
        **request.form,
        'users_id': session['user_id']
    }
    Vehicle.save(vehicle_data)
    return redirect('/dashboard')
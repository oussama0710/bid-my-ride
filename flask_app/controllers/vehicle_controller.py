from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user_model import User
from flask_app.models.vehicle_model import Vehicle
#=============DISPLAY ROUTE==============================
@app.route('/products/new')
def new_product():
    if 'user_id' not in session :#=================bch tekml problem BD(and usere.role)==============
        return redirect('/')
    return render_template('add_product.html')
#============================ACTION ROUTE================================
@app.route('/products/add', methods=['POST'])
def add_product():
    if not Vehicle.validate_vehicle(request.form):
        return redirect('/product/new')
    data = {
        **request.form,
        'user_id': session['user_id']#=================bch tekml problem BD(and usere.role)==============
    }
    Vehicle.save_vehicle(data)
    return redirect('/')
from flask import request, render_template, redirect, session
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('addUser.html')

@app.route('/user/new', methods=['POST'])
def create_user():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
    }
    User.save(data)
    return redirect('/users')

@app.route('/users')
def all_users():
    users = User.get_all()
    #print(f"Testing: {users}")
    return render_template('show.html', users = users)
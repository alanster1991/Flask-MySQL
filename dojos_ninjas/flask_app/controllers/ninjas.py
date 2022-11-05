from flask import render_template, request, redirect
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos = dojo.Dojo.get_All())

@app.route('/new/ninja', methods=['POST'])
def new_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')
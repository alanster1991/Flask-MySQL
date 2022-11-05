from flask_app import app
from flask import request, render_template, redirect
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_All()
    return render_template("index.html", all_dojos = dojos )

@app.route('/new/dojo', methods=["POST"])
def newDojo():
    Dojo.save(request.form)
    return redirect('/dojos' )


@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id" : id
    }

    return render_template('dojo.html', dojo = Dojo.get_dojo_with_ninjas(data) )



from flask import Flask, request, redirect, render_template
from user import User

app = Flask(__name__)
app.secret_key = "call me maybe"

@app.route('/')
def add_user():
    return render_template('add_user.html')

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
    return render_template('all_users.html', users = users)

if __name__ == "__main__":
    app.run(debug=True)

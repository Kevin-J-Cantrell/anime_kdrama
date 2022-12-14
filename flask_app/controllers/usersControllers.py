from flask_app import app
from flask import Flask, redirect, session, request, render_template, url_for, flash
from flask_app.models.users import User
from flask_app.models.recipes import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def Register_page():
    
    return render_template ("register_login.html")

@app.route('/dashboard')
def Dashboard():
    print('finding user')
    print(session['user_id'])
    id = {
        'id':session['user_id'] 
        } 
    if 'user_id' not in session:
        return redirect('/')
    recipes=Recipe.get_all()
    users=User.get_one(id)
    return render_template ("Dashboard.html",users=users,recipes=recipes)

@app.route('/register', methods=['POST'])
def Register():
    if not User.validate_register(request.form):
        return redirect ("/")
    data = {
        'first_name':request.form['first_name'],
        'last_name' :request.form['last_name'],
        'email'     :request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])

    }
    session['user_id'] = User.create(data)
    return redirect ("/dashboard")

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    print(user_in_db)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", "login")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    print(user_in_db.id)
    # never render on a post!!!
    return redirect("/dashboard")

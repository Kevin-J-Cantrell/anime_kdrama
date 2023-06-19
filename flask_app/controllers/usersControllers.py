import pprint
from AnilistPython import Anilist
import requests
import urllib.parse
from flask_app import app
from flask import Flask, redirect, session, request, render_template, url_for, flash
from flask_app.models.users import User
from flask_app.models.animes import Anime
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def Login():

    return render_template("login.html")


@app.route('/register-page')
def Register_Page():

    return render_template("register.html")


@app.route('/dashboard')
def Dashboard():
    print('finding user')
    print(session['user_id'])
    id = {
        'id': session['user_id']
    }
    if 'user_id' not in session:
        return redirect('/')
    # animes = Anime.get_all()
    users = User.get_one(id)
    url = "https://myanimelist.p.rapidapi.com/anime/top/all"

    headers = {
        "X-RapidAPI-Key": "8242de165dmsh4e2d1c1cfeef870p19ca8fjsn6398a61dd3ad",
        "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    pprint.pprint(data)
    # for item in data:
    #     api_data = {
    #         'id': item['myanimelist_id'],
    #         'picture_url':item['picture_url'],
    #         'title' : item['title'],
    #         "type" : item ["type"],
    #         'aired_on' : item['aired_on'],
    #         'score' : item['score'],
    #         'myanimelist_id' : item['myanimelist_id'],
    #         'myanimelist_url' : item['myanimelist_url'],
    #         'rank' : item['rank'],
    #         'members' : item['members'],
    #         # 'user_id' : session.item['user_id'],
    #         }
    #     new_anime = Anime(api_data)
    # Anime.db.session.create(new_anime)


    # # Commit the changes to the database
    # Anime.db.session.commit()
    print(data)

    return render_template("Dashboard.html", users=users, animes=data)


@app.route('/register', methods=['POST'])
def Register():
    if not User.validate_register(request.form):
        return redirect("/")
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])

    }
    session['user_id'] = User.create(data)
    return redirect("/dashboard")


@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = {"email": request.form["email"]}
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

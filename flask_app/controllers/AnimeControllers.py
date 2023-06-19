from re import search
from AnilistPython import Anilist
import cgi
import requests
from urllib.parse import urlencode
from flask_app import app
from flask import Flask, redirect, session, request, render_template, url_for, flash
from flask_app.models.animes import Anime
from flask_app.models.users import User
from flask import flash
anilist = Anilist()


@app.route('/anime/page')
def Anime_Page():



    return render_template ("anime.html")


@app.route('/anime/search', methods=['GET', 'POST'])
def Anime_Search():
    if request.method == 'POST':
        search_query = request.form['search_query']
        
        # Results a list of three dictionaries 
        anime_res = anilist.get_anime(search_query, deepsearch=True, count=3)
        
        
        print(anime_res)

    return render_template ("anime.html" , srch = anime_res )
    

# ---------------------------------------------------------------
@app.route('/posted/info/<int:id>')
def Posted_info(id):
    
    animes=Anime.anime_id(id)
    users=User.get_one({'id':session['user_id']})
    return render_template ("posted_info.html",users=users,animes=animes )


# @app.route('/edit/anime/page/<int:id>')
# def edit_page(id):
    
    
#     return render_template ("edit_anime.html", animes=Anime.get_one(id))

# @app.route('/edit/anime', methods=['POST'])
# def edit_Anime():
#     if not Anime.edit_user_msgs(request.form):
#         return redirect(f"/edit/anime/page")
#     data = {
#         'id': request.form['id'],
#         'name': request.form['name'],   
#         'description':request.form['description'],
#         'instruction': request.form['instruction'],
#         'date_posted': request.form['date_posted'],
#         'under_time': request.form['under_time'],
#     }
#     Anime.update(data)
#     return redirect ("/dashboard")

# @app.route('/add/anime', methods=['POST'])
# def add_Anime():
#     if not Anime.edit_user_msgs(request.form):
#         return redirect("/add/anime/page")
#     data = {
#         'name': request.form['name'],   
#         'description':request.form['description'],
#         'instruction': request.form['instruction'],
#         'date_posted': request.form['date_posted'],
#         'under_time': request.form['under_time'],
#         'user_id': request.form['user_id'],
#     }
#     Anime.create(data)
#     return redirect ("/dashboard")

# @app.route('/delete/anime/<int:id>')
# def delete_Anime(id):
    
#     Anime.delete(id)
#     return redirect ("/dashboard")


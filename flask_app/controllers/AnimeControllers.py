from re import search
import cgi
import requests
from urllib.parse import urlencode
from flask_app import app
from flask import Flask, redirect, session, request, render_template, url_for, flash
from flask_app.models.animes import Anime
from flask_app.models.users import User
from flask import flash

@app.route('/anime/page')
def Anime_Page():

    # url = "https://myanimelist.p.rapidapi.com/anime/top/all"

    # headers = {
    #     "X-RapidAPI-Key": "8242de165dmsh4e2d1c1cfeef870p19ca8fjsn6398a61dd3ad",
    #     "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
    # }
    
    # response = requests.get(url, headers=headers )
    # result = response.json()
    # print(result)
    
    # , 
    
   
    return render_template ("anime.html")


@app.route('/anime/search', methods=['GET', 'POST'])
def Anime_Search():
    if request.method == 'POST':
        search_query = request.form['search_query']
        url = f"https://myanimelist.p.rapidapi.com/anime/search/{search_query}/5"
        headers = {
            "X-RapidAPI-Key": "8242de165dmsh4e2d1c1cfeef870p19ca8fjsn6398a61dd3ad",
            "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
        }
    
        response = requests.get(url, headers=headers)
        
        results = response.json()
        print(results)
        result = results
        # data = {
        #     "title": result["title"],
        #     "description":result["description"],
        #     # "aired_on": result["aired_on"],
        #     # "type": result["type"],
        #     "picture_url": result["picture_url"],
        #     "myanimelist_id": result["myanimelist_id"],
        #     "myanimelist_url": result["myanimelist_url"],
        #     # "user_id": session['user_id'],
        # }
        # print(data)
        
 
    return render_template ("anime.html" , srch = results )
    

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


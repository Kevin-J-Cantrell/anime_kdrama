from flask_app import app
from flask import Flask, redirect, session, request, render_template, url_for, flash
from flask_app.models.chinese_animes import ChineseAnime
from flask_app.models.users import User
from flask import flash

@app.route('/chinese/anime/page')
def ChineseAnime_Page():
    
    
    return render_template ("chinese_anime.html",chinese_animes=ChineseAnime.get_all())

# @app.route('/posted/info/<int:id>')
# def Posted_info(id):
    
#     chinese_animes=ChineseAnime.anime_id(id)
#     users=User.get_one({'id':session['user_id']})
#     return render_template ("posted_info.html",users=users,chinese_animes=chinese_animes )


# @app.route('/edit/anime/page/<int:id>')
# def edit_page(id):
    
    
#     return render_template ("edit_anime.html", chinese_animes=ChineseAnime.get_one(id))

# @app.route('/edit/anime', methods=['POST'])
# def edit_Anime():
#     if not ChineseAnime.edit_user_msgs(request.form):
#         return redirect(f"/edit/anime/page")
#     data = {
#         'id': request.form['id'],
#         'name': request.form['name'],   
#         'description':request.form['description'],
#         'instruction': request.form['instruction'],
#         'date_posted': request.form['date_posted'],
#         'under_time': request.form['under_time'],
#     }
#     ChineseAnime.update(data)
#     return redirect ("/dashboard")

# @app.route('/add/anime', methods=['POST'])
# def add_Anime():
#     if not ChineseAnime.edit_user_msgs(request.form):
#         return redirect("/add/anime/page")
#     data = {
#         'name': request.form['name'],   
#         'description':request.form['description'],
#         'instruction': request.form['instruction'],
#         'date_posted': request.form['date_posted'],
#         'under_time': request.form['under_time'],
#         'user_id': request.form['user_id'],
#     }
#     ChineseAnime.create(data)
#     return redirect ("/dashboard")

# @app.route('/delete/Anime/<int:id>')
# def delete_Anime(id):
    
#     ChineseAnime.delete(id)
#     return redirect ("/dashboard")


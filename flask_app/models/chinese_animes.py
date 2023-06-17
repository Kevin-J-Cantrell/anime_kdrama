from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import users
from flask import flash

class ChineseAnime:
    db = 'DaList_Site'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description  = data['description']
        self.date_posted  = data['date_posted']
        self.want_to_watch  = data['want_to_watch']
        self.not_sure  = data['not_sure']
        self.wont_watch  = data['wont_watch']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM chinese_animes
        JOIN users
        ON chinese_animes.user_id = users.id;"""
        anime_data = connectToMySQL(cls.db).query_db(query)
        output = []
        for user_info in anime_data:
            my_anime = cls (user_info)
            user_data = {
                "id" : user_info["users.id"],
                "first_name" : user_info["first_name"],
                "last_name" : user_info["last_name"],
                "email" : user_info["email"],
                "password" : user_info["password"],
                "created_at" : user_info["users.created_at"],
                "updated_at" : user_info["users.updated_at"]
            }
            my_anime.user = users.User(user_data)# goes to user.py
            output.append( my_anime)
        return output
    
    @classmethod
    def create(cls, data ):
        query = """
        INSERT INTO chinese_animes ( title , description , date_posted ,want_to_watch,not_sure,wont_watch,user_id ) 
        VALUES ( %(title)s , %(description)s , %(date_posted)s , %(want_to_watch)s , %(not_sure)s , %(date_posted)s , %(user_id)s );"""
        result = connectToMySQL(cls.db).query_db( query, data )
        return result
    
    @classmethod
    def delete(cls,id):
        data = {"id" : id}
        query = "DELETE FROM chinese_animes WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db( query,data )

    @classmethod
    def update(cls,data):
        print("updating")
        query = """
        UPDATE chinese_animes 
        SET name = %(title)s , description = %(description)s , date_posted = %(date_posted)s ,want_to_watch= %(want_to_watch)s , not_sure= %(not_sure)s,wont_watch= %(wont_watch)s
        WHERE id = %(id)s;"""
        connectToMySQL(cls.db).query_db( query,data )
        
    @classmethod
    def get_one(cls,id):
        data = {"id": id}
        query = "SELECT * FROM chinese_animes WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db( query,data )
        return cls(result[0]) # a list of dictionaries
    
    @classmethod
    def chinese_anime_user(cls ,anime_id):#joining chinese_anime to user
        data = {"id": anime_id }
        query = """
        SELECT * FROM chinese_animes
        JOIN users
        ON chinese_animes.user_id = users.id
        WHERE chinese_animes.id = %(id)s
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        user_info = results[0]
        my_anime = cls (user_info)
        user_data = {
            "id" : user_info["users.id"],
            "first_name" : user_info["first_name"],
            "last_name" : user_info["last_name"],
            "email" : user_info["email"],
            "password" : user_info["password"],
            "created_at" : user_info["users.created_at"],
            "updated_at" : user_info["users.updated_at"]
        }
        my_anime.user = users.User(user_data)# goes to user.py
        return my_anime
    
    @staticmethod
    def edit_user_msgs(user):
        is_valid = True
        if len(user['name']) < 5:
            flash("First name must be at least 5 characters")
            is_valid= False
        if len(user['description']) < 2:
            flash("Description field can not be empty")
            is_valid= False
        if len(user['date_posted']) < 2:
            flash("Date can not be empty")
            is_valid= False
        return is_valid
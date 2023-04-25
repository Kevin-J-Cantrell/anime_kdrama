from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import users
from flask import flash

class Recipe:
    mydb = 'recipes_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description  = data['description']
        self.instruction  = data['instruction']
        self.date_posted  = data['date_posted']
        self.under_time  = data['under_time']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM recipes
        JOIN users
        ON recipes.user_id = users.id;"""
        recipe_data = connectToMySQL(cls.mydb).query_db(query)
        output = []
        for user_info in recipe_data:
            my_recipe = cls (user_info)
            user_data = {
                "id" : user_info["users.id"],
                "first_name" : user_info["first_name"],
                "last_name" : user_info["last_name"],
                "email" : user_info["email"],
                "password" : user_info["password"],
                "created_at" : user_info["users.created_at"],
                "updated_at" : user_info["users.updated_at"]
            }
            my_recipe.user = users.User(user_data)# goes to user.py
            output.append( my_recipe)
        return output
    
    @classmethod
    def create(cls, data ):
        query = """
        INSERT INTO recipes ( name , description , instruction , date_posted , under_time ,user_id ) 
        VALUES ( %(name)s , %(description)s , %(instruction)s , %(date_posted)s , %(under_time)s , %(user_id)s );"""
        result = connectToMySQL(cls.mydb).query_db( query, data )
        return result
    
    @classmethod
    def delete(cls,id):
        data = {"id" : id}
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        connectToMySQL(cls.mydb).query_db( query,data )

    @classmethod
    def update(cls,data):
        print("updating")
        query = """
        UPDATE recipes 
        SET name = %(name)s , description = %(description)s , instruction = %(instruction)s , date_posted = %(date_posted)s , under_time = %(under_time)s 
        WHERE id = %(id)s;"""
        connectToMySQL(cls.mydb).query_db( query,data )
        
    @classmethod
    def get_one(cls,id):
        data = {"id": id}
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL(cls.mydb).query_db( query,data )
        return cls(result[0]) # a list of dictionaries
    
    @classmethod
    def rcp_user(cls ,rcp_id):
        data = {"id": rcp_id }
        query = """
        SELECT * FROM recipes
        JOIN users
        ON recipes.user_id = users.id
        WHERE recipes.id = %(id)s
        """
        results = connectToMySQL(cls.mydb).query_db(query,data)
        print(results)
        user_info = results[0]
        my_recipe = cls (user_info)
        user_data = {
            "id" : user_info["users.id"],
            "first_name" : user_info["first_name"],
            "last_name" : user_info["last_name"],
            "email" : user_info["email"],
            "password" : user_info["password"],
            "created_at" : user_info["users.created_at"],
            "updated_at" : user_info["users.updated_at"]
        }
        my_recipe.user = users.User(user_data)# goes to user.py
        return my_recipe
    
    @staticmethod
    def edit_recipe_msgs(recipe):
        is_valid = True
        if len(recipe['name']) < 5:
            flash("First name must be at least 5 characters")
            is_valid= False
        if len(recipe['description']) < 2:
            flash("Description field can not be empty")
            is_valid= False
        if len(recipe['instruction']) < 2:
            flash("instruction field can not be empty")
            is_valid= False
        if len(recipe['date_posted']) < 2:
            flash("Date can not be empty")
            is_valid= False
        return is_valid
from flask_app import app
from flask_app.controllers import ChineseAnimeControllers
from flask_app.controllers import usersControllers
from flask_app.controllers import AnimeControllers


if __name__ == '__main__':
    app.run(debug=True, port=8000)
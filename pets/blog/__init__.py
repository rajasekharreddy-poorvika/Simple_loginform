from flask import Flask
from blog.home.views import pet
from blog.home.models import db




app = Flask(__name__)
db.init_app(app)


app.config.from_pyfile('config.py')
app.register_blueprint(home.views.pet)

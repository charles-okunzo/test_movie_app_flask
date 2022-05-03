from flask import Flask
from config import config_options
from flask_bootstrap  import Bootstrap
from flask_sqlalchemy import SQLAlchemy


bootstrap = Bootstrap()
db = SQLAlchemy()

#app factory function
def create_app(config_name):

  #Initializing application
  app = Flask(__name__)

  #setting up configurations
  app.config.from_object(config_options[config_name])

  #registering blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  #setting config
  from .request import configure_request
  configure_request(app)

  #initializing flask extension
  bootstrap.init_app(app)
  db.init_app(app)
  return app
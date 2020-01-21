from flask import Flask
from models import db
from route import blueprint

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin1234@localhost:3306/test'
db.init_app(application)
application.register_blueprint(blueprint)

if __name__ == '__main__':
    application.run(debug=True)
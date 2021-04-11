import flask
from flask_restful import Api
from db import db
from resources.create_update_audio import CreateAPI, UpdateAPI
from resources.get_delete_audio import RetrieveAndDeleteAPI, RetrieveAll
from config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)

# app.config["DEBUG"] = True
#
# USR = 'root'
# PWD = 'mohan1111'
#
# SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@localhost:3306/exercise'.format(USR, PWD)
# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(RetrieveAndDeleteAPI, '/<string:audio_type>/<string:audio_id>')
api.add_resource(CreateAPI, '/<string:audio_type>')
api.add_resource(UpdateAPI, '/<string:audio_type>/<string:audio_id>')
api.add_resource(RetrieveAll, '/<string:audio_type>')

if __name__ == '__main__':
    db.init_app(app)
    app.run()

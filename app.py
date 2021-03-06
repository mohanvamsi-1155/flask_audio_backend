import flask
from flask_restful import Api
from db import db
from resources.create_update_audio import CreateAPI, UpdateAPI
from resources.get_delete_audio import RetrieveAndDeleteAPI, RetrieveAll
from config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)

api = Api(app)
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(RetrieveAndDeleteAPI, '/<string:audio_type>/<string:audio_id>')
api.add_resource(CreateAPI, '/<string:audio_type>')
api.add_resource(UpdateAPI, '/<string:audio_type>/<string:audio_id>')
api.add_resource(RetrieveAll, '/<string:audio_type>')

if __name__ == '__main__':
    app.run()

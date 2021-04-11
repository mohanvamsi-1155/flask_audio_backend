from flask_restful import Resource

from models.audiobook import AudiobookModel
from models.podcast import PodcastModel
from models.song import SongModel


class RetrieveAndDeleteAPI(Resource):
    def get(self, audio_type, audio_id):  # get
        if audio_type.lower() == 'song':
            song = SongModel.find_by_id(audio_id)
            if song:
                return song.json()
        elif audio_type.lower() == 'podcast':
            podcast = PodcastModel.find_by_id(audio_id)
            if podcast:
                return podcast.json()
        elif audio_type.lower() == 'audiobook':
            audiobook = AudiobookModel.find_by_id(audio_id)
            if audiobook:
                return audiobook.json()
        else:
            return {'errorMessage': 'Invalid audio file type'}, 400
        return {'errorMessage': 'audio file not found'}, 404

    def delete(self, audio_type, audio_id):  # delete
        if audio_type.lower() == 'song':
            song = SongModel.find_by_id(audio_id)
            if song:
                return song.delete_from_db()
        elif audio_type.lower() == 'podcast':
            podcast = PodcastModel.find_by_id(audio_id)
            if podcast:
                return podcast.delete_from_db()
        elif audio_type.lower() == 'audiobook':
            audiobook = AudiobookModel.find_by_id(audio_id)
            if audiobook:
                return audiobook.delete_from_db()
        else:
            return {'errorMessage': 'Invalid audio file type'}, 400
        return {'errorMessage': 'audio file not found'}, 404


class RetrieveAll(Resource):
    def get(self, audio_type):
        if audio_type.lower() == 'song':
            return {'songs': [song.json() for song in SongModel.query.all()]}
        elif audio_type.lower() == 'podcast':
            return {'podcasts': [podcast.json() for podcast in PodcastModel.query.all()]}
        elif audio_type.lower() == 'audiobook':
            return {'audiobooks': [audiobook.json() for audiobook in AudiobookModel.query.all()]}
        else:
            return {'errorMessage': 'Invalid audio Type'}, 400


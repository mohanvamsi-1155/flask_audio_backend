from datetime import datetime

from flask_restful import Resource, reqparse

import validations
from models.audiobook import AudiobookModel
from models.podcast import PodcastModel
from models.song import SongModel

song_parser = reqparse.RequestParser()
podcast_parser = reqparse.RequestParser()
audiobook_parser = reqparse.RequestParser()

song_parser.add_argument('ID', type=int, required=True)
song_parser.add_argument('song_name', type=validations.length_check(100), required=True)
song_parser.add_argument('duration', type=validations.duration_check(), required=True)
song_parser.add_argument('uploaded_time', type=validations.datetime_check(), required=True)

podcast_parser.add_argument('ID', type=int, required=True)
podcast_parser.add_argument('podcast_name', type=validations.length_check(100), required=True)
podcast_parser.add_argument('duration_in_secs', type=validations.duration_check(), required=True)
podcast_parser.add_argument('uploaded_time', type=validations.datetime_check(), required=True)
podcast_parser.add_argument('host', type=validations.length_check(100), required=True)
podcast_parser.add_argument('participants', type=validations.list_check())

audiobook_parser.add_argument('ID', type=int, required=True)
audiobook_parser.add_argument('title', type=validations.length_check(100), required=True)
audiobook_parser.add_argument('author', type=validations.length_check(100), required=True)
audiobook_parser.add_argument('narrator', type=validations.length_check(100), required=True)
audiobook_parser.add_argument('duration', type=validations.duration_check(), required=True)
audiobook_parser.add_argument('uploaded_time', type=validations.datetime_check(), required=True)


class CreateAPI(Resource):
    def post(self, audio_type):
        if audio_type.lower() == 'song':
            data = song_parser.parse_args()
            data['uploaded_time'] = datetime.strptime(data['uploaded_time'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime('%Y-%m-%d %H:%M:%S')
            song = SongModel.find_by_id(data['ID'])
            if song is None:
                song = SongModel(**data)
            else:
                return {'errorMessage': 'Duplicate ID'}, 400

            try:
                SongModel.save_to_db(song)
            except Exception as e:
                print(e)
                return {'errorMessage': 'Internal Error Occurred'}, 500

            return song.json(), 201
        elif audio_type.lower() == 'podcast':
            data = podcast_parser.parse_args()
            data['uploaded_time'] = datetime.strptime(data['uploaded_time'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime('%Y-%m-%d %H:%M:%S')
            podcast = PodcastModel.find_by_id(data['ID'])
            if podcast is None:
                podcast = PodcastModel(**data)
            else:
                return {'errorMessage': 'Duplicate ID'}, 400

            try:
                PodcastModel.save_to_db(podcast)
            except Exception as e:
                print(e)
                return {'errorMessage': 'Internal Error Occurred'}, 500

            return podcast.json(), 201
        elif audio_type.lower() == 'audiobook':
            data = audiobook_parser.parse_args()
            data['uploaded_time'] = datetime.strptime(data['uploaded_time'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime('%Y-%m-%d %H:%M:%S')
            audiobook = AudiobookModel.find_by_id(data['ID'])
            if audiobook is None:
                audiobook = AudiobookModel(**data)
            else:
                return {'errorMessage': 'Duplicate ID'}, 400

            try:
                AudiobookModel.save_to_db(audiobook)
            except Exception as e:
                print(e)
                return {'errorMessage': 'Internal Error Occurred'}, 500

            return audiobook.json(), 201
        else:
            return {'errorMessage': 'Invalid audio type'}, 400


class UpdateAPI(Resource):
    def put(self, audio_type, audio_id):
        if audio_type.lower() == 'song':
            data = song_parser.parse_args()
            song = SongModel.find_by_id(audio_id)
            data['uploaded_time'] = datetime.strptime(data['uploaded_time'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime(
                '%Y-%m-%d %H:%M:%S')
            if song is None:
                song = SongModel(**data)
            else:
                song.song_name = data['song_name']
                song.duration = data['duration']
                song.uploaded_time = data['uploaded_time']

            try:
                SongModel.save_to_db(song)
            except Exception as e:
                print(e)
                return {'errorMessage': 'Internal Error Occurred'}, 500

            return song.json()
        elif audio_type.lower() == 'podcast':
            data = podcast_parser.parse_args()
            podcast = PodcastModel.find_by_id(audio_id)
            data['uploaded_time'] = datetime.strptime(data['uploaded_time'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime(
                '%Y-%m-%d %H:%M:%S')

            if podcast is None:
                podcast = PodcastModel(**data)
            else:
                podcast.podcast_name = data['podcast_name']
                podcast.duration_in_secs = data['duration_in_secs']
                podcast.uploaded_time = data['uploaded_time']
                podcast.host = data['uploaded_time']
                podcast.participants = data['participants']

            try:
                PodcastModel.save_to_db(podcast)
            except Exception as e:
                print(e)
                return {'errorMessage': 'Internal Error Occurred'}, 500

            return podcast.json()
        elif audio_type.lower() == 'audiobook':
            data = audiobook_parser.parse_args()
            audiobook = AudiobookModel.find_by_id(audio_id)
            data['uploaded_time'] = datetime.strptime(data['uploaded_time'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime(
                '%Y-%m-%d %H:%M:%S')

            if audiobook is None:
                audiobook = AudiobookModel(**data)
            else:
                audiobook.title = data['title']
                audiobook.author = data['author']
                audiobook.narrator = data['narrator']
                audiobook.duration = data['duration']
                audiobook.uploaded_time = data['uploaded_time']

            try:
                AudiobookModel.save_to_db(audiobook)
            except Exception as e:
                print(e)
                return {'errorMessage': 'Internal Error Occurred'}, 500

            return audiobook.json()
        else:
            return {'errorMessage': 'Invalid audio type'}, 400

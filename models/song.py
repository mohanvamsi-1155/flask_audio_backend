from db import db


class SongModel(db.Model):
    __tablename__ = 'song'
    ID = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(101), nullable=True)
    duration = db.Column(db.Integer, nullable=True)
    uploaded_time = db.Column(db.DateTime, nullable=True)

    def __init__(self, ID, song_name, duration, uploaded_time):
        self.ID = ID
        self.song_name = song_name
        self.duration = duration
        self.uploaded_time = uploaded_time

    def json(self):
        return {'ID': self.ID, 'song_name': self.song_name, 'duration': self.duration,
                'uploaded_time': str(self.uploaded_time)}

    @classmethod
    def find_by_id(cls, audio_id):
        return SongModel.query.filter_by(ID=audio_id).first()

    @staticmethod
    def save_to_db(song):
        db.session.add(song)
        db.session.commit()

    @staticmethod
    def delete_from_db(song):
        db.session.delete(song)
        db.session.commit()

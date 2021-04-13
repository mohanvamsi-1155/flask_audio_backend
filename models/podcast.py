from db import db


class PodcastModel(db.Model):
    __tablename__ = 'podcast'
    ID = db.Column(db.Integer, primary_key=True)
    podcast_name = db.Column(db.String(101), nullable=True)
    duration_in_secs = db.Column(db.Integer, nullable=True)
    uploaded_time = db.Column(db.DateTime, nullable=True)
    host = db.Column(db.String(101), nullable=True)
    participants = db.Column(db.Text)

    def __init__(self, ID, podcast_name, duration_in_secs, uploaded_time, host, participants):
        self.ID = ID
        self.podcast_name = podcast_name
        self.duration_in_secs = duration_in_secs
        self.uploaded_time = uploaded_time
        self.host = host
        self.participants = participants

    def json(self):
        return {'ID': self.ID, 'podcast_name': self.podcast_name, 'duration_in_secs': self.duration_in_secs,
                'uploaded_time': str(self.uploaded_time), 'host': self.host, 'participants': self.participants}

    @classmethod
    def find_by_id(cls, audio_id):
        return PodcastModel.query.filter_by(ID=audio_id).first()

    @staticmethod
    def save_to_db(podcast):
        db.session.add(podcast)
        db.session.commit()

    @staticmethod
    def delete_from_db(podcast):
        db.session.delete(podcast)
        db.session.commit()

from db import db


class AudiobookModel(db.Model):
    __tablename__ = 'audiobook'
    ID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(101), nullable=True)
    author = db.Column(db.String(101), nullable=True)
    narrator = db.Column(db.String(101), nullable=True)
    duration = db.Column(db.Integer, nullable=True)
    uploaded_time = db.Column(db.DateTime, nullable=True)

    def __init__(self,ID, title, author, narrator, duration, uploaded_time):
        self.ID = ID
        self.title = title
        self.author = author
        self.narrator = narrator
        self.duration = duration
        self.uploaded_time = uploaded_time

    def json(self):
        return {'ID': self.ID, 'title': self.title, 'author': self.author,
                'narrator': self.narrator, 'duration': self.duration, 'uploaded_time': str(self.uploaded_time)}

    @classmethod
    def find_by_id(cls, audio_id):
        return AudiobookModel.query.filter_by(ID=audio_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

import pytest

from models.song import SongModel
from datetime import datetime


@pytest.fixture
def song():
    params = {'ID': 1001, 'song_name': 'mohan', 'duration': 2331, 'uploaded_time': datetime.today()}
    song = SongModel(**params)
    return song


def test_song_duration(song):
    assert song.duration == 2331


def test_song_ID(song):
    assert song.ID == 1001


def test_song_name(song):
    assert song.song_name == 'mohan'

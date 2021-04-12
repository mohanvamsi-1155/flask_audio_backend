import pytest

from datetime import datetime

from models.audiobook import AudiobookModel


@pytest.fixture
def audiobook():
    params = {'ID': 1001, 'title': 'mohan', 'author': 'stacey', 'narrator': 'ron', 'duration': 2331,
              'uploaded_time': datetime.today()}
    audiobook = AudiobookModel(**params)
    return audiobook


def test_audiobook_duration(audiobook):
    assert audiobook.duration == 2331


def test_audiobook_ID(audiobook):
    assert audiobook.ID == 1001


def test_audiobook_title(audiobook):
    assert audiobook.title == 'mohan'


def test_audiobook_author(audiobook):
    assert audiobook.author == 'stacey'


def test_audiobook_narrator(audiobook):
    assert audiobook.narrator == 'ron'

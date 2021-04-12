from datetime import datetime

import pytest

from models.podcast import PodcastModel


@pytest.fixture
def podcast():
    params = {'ID': 1001, 'podcast_name': 'mohan', 'duration_in_secs': 2331, 'uploaded_time': datetime.today(),
              'host': 'ABC', 'participants': 'a,b,c'}
    podcast = PodcastModel(**params)
    return podcast


def test_podcast_duration(podcast):
    assert podcast.duration_in_secs == 2331


def test_podcast_ID(podcast):
    assert podcast.ID == 1001


def test_podcast_name(podcast):
    assert podcast.podcast_name == 'mohan'


def test_podcast_host(podcast):
    assert podcast.host == 'ABC'

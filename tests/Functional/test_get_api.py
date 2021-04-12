def test_get_song_success(app, client):
    res = client.get('/Song/2')
    assert res.status_code == 200


def test_get_song_invalid_audio(app, client):
    res = client.get('/ABC/2')
    assert res.status_code == 400


def test_get_song_id_not_found(app,client):
    res = client.get('Song/1001')
    assert res.status_code == 404

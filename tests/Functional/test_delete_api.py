def test_delete_success(app, client):
    res = client.delete('/Song/1')
    assert res.status_code == 200


def test_delete_success_audiobook(app, client):
    res = client.delete('/Audiobook/3')
    assert res.status_code == 200


def test_delete_invalid_audio(app, client):
    res = client.delete('/ABC/2')
    assert res.status_code == 400


def test_delete_id_not_found(app, client):
    res = client.delete('/Podcast/1001')
    assert res.status_code == 404

def test_get_health(web_client):
    response = web_client.get('/balance/health')

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {'message': 'OK'}

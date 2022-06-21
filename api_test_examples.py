import requests


def test_http_get_status_code_should_be_200():
    response = requests.get('http://api.zippopotam.us/us/90210')
    assert response.status_code == 200


def test_response_body_element_should_match_expected_value():
    response = requests.get('http://api.zippopotam.us/us/90210')
    response_body = response.json()
    assert response_body['places'][0]['place name'] == 'Beverly Hills'


def test_http_post_status_code_should_be_201():
    new_post = {
        'userId': 1,
        'title': 'My post title',
        'body': 'This is the body of my post'
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
    assert response.status_code == 201
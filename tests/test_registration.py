import requests
from http import HTTPStatus
import api.questions_api import api

def registration():
    url = 'https://reqres.in/api/register'
    email = 'eve.holt@reqres.in'
    password = '  '
    res = api.questions_api.registration(email, password)

    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['email'] == email
    assert res.json()['password'] == password

    assert api.delete_user(res.json()(['id']).status_code == HTTPStatus.NO_CONTENT


    response = requests.get(url)
    assert response.status_code == HTTPStatus.OK  # 200

def registration_inc():
    url = 'https://reqres.in/api/register'
    email = 'eve.holt@reqres.in'

    res = api.questions_api.registration(password)

        assert res.status_code == HTTPStatus.CREATED
        assert res.json()['email'] == email

        assert api.delete_user(res.json()(['id']).status_code == HTTPStatus.NO_CONTENT

        response = requests.get(url)
        assert response.status_code == 400
print ('error:Missing password")
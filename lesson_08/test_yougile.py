import pytest
import requests
import json
base_url = "https://ru.yougile.com/api-v2"
my_headers = {
    'Authorization': 'Bearer 8aRHXEY8DRZq93j5l45SViGQqm3Vx+R1d3UzqikwEScvHek3oVt6P87r4J-qiBoI',
    'Content-Type': 'application/json'
}
negative_headers = {
    'Authorization': '8aRHXEY8DRZq93j5l45SViGQqm3Vx+R1d3UzqikwEScvHek3oVt6P87r4J-qiBoI',
    'Content-Type': 'application/json'
}
valid_project_data = {
  'title': "Мобис",
  'users': {
    '44f0cba9-28b7-46a6-853f-025319b9876c': 'admin'
  }
}
invalid_project_data = {
  'title': ""
}
# позитивная проверка
def test_get_projects_positiv():
    response = requests.get(base_url + '/projects', headers = my_headers)
    assert response.status_code == 200

# негативная проверка
def test_get_projects_negative():
    response = requests.get(base_url + '/projects', headers = negative_headers)
    assert response.status_code == 401

# позитивная проверка
def test_create_project_positiv():
    response = requests.post(base_url + '/projects',json = valid_project_data, headers = my_headers)
    assert response.status_code == 201
    project_id = response.json()["id"]

# негативная проверка
def test_create_project_negativ():
    response = requests.post(base_url + '/projects',json = invalid_project_data, headers = my_headers)
    assert response.status_code == 400

# позитивная проверка
def test_get_project_by_id_positiv():
     response = requests.get("https://ru.yougile.com/api-v2/projects/bf0a32aa-4eaa-4f43-8a08-1defa0a53522", headers = my_headers)
     assert response.status_code == 200

# негативная проверка
def test_get_project_by_id_negative():
     response = requests.get("https://ru.yougile.com/api-v2/projects/bf0a32aa", headers = my_headers)
     assert response.status_code == 404


# позитивная проверка
def test_update_project_positiv():
    data = {
        'deleted': 'true',
  "title": "Мобис",
  'users': {
    '44f0cba9-28b7-46a6-853f-025319b9876c': 'admin'
  }
    }
    response = requests.get("https://ru.yougile.com/api-v2/projects/bf0a32aa-4eaa-4f43-8a08-1defa0a53522", json = data, headers = my_headers)
    assert response.status_code == 200

# негативная проверка
def test_update_project_negative():
    data = {
    }
    response = requests.get("https://ru.yougile.com/api-v2/projects/bf0a32aa-4eaa-4f43-8a08-1defa0a535", json = data, headers = my_headers)
    assert response.status_code == 404

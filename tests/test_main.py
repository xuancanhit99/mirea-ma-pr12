import requests

api_url = 'http://localhost:8000'


def test_healthcheck():
    response = requests.get(f'{api_url}/__health')
    assert response.status_code == 200


class TestStudents():
    def test_get_empty_stu(self):
        response = requests.get(f'{api_url}/v1/stu')
        assert response.status_code == 200
        assert len(response.json()) == 0

    def test_create_stu(self):
        body = {"name": "Xuan Canh", "age": "24", "math": "100", "literature": "80", "english": "90"}
        response = requests.post(f'{api_url}/v1/stu', json=body)
        assert response.status_code == 200
        assert response.json().get('name') == 'Xuan Canh'
        assert response.json().get('age') == '24'
        assert response.json().get('math') == '100'
        assert response.json().get('literature') == '80'
        assert response.json().get('english') == '90'
        assert response.json().get('id') == '0'

    def test_get_stu_by_id(self):
        response = requests.get(f'{api_url}/v1/stu/0')
        assert response.status_code == 200
        assert response.json().get('name') == 'Xuan Canh'
        assert response.json().get('age') == '24'
        assert response.json().get('math') == '100'
        assert response.json().get('literature') == '80'
        assert response.json().get('english') == '90'
        assert response.json().get('id') == '0'

    def test_get_not_empty_stu(self):
        response = requests.get(f'{api_url}/v1/stu')
        assert response.status_code == 200
        assert len(response.json()) == 1

    def test_get_stu_by_id_2(self):
        response = requests.get(f'{api_url}/v1/stu/0')
        assert response.status_code == 200
        assert response.json().get('name') == 'Xuan Canh'
        assert response.json().get('age') == '24'
        assert response.json().get('math') == '10'
        assert response.json().get('literature') == '80'
        assert response.json().get('english') == '90'
        assert response.json().get('id') == '0'



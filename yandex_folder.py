import requests

headers = {
    'Authorization': '<TOKEN>'
}
url = 'https://cloud-api.yandex.net/v1/disk/resources'


def folder(name: str):
    params = {'path': name}
    response = requests.put(f"{url}", params=params, headers=headers)
    return response.status_code

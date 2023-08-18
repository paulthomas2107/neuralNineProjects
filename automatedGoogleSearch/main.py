import requests

bollox1 = 112
bollox2 = 222

search_query = 'football'

url = 'https://www.googleapis.com/customsearch/v1'

params = {
    'q': search_query,
    'key': bollox1,
    'cx': bollox2,
    # 'searchType': "image",
    # 'dateRestrict': "2021-01-01:2016-12-31",
    # 'fileType': 'pdf'
    'lr': 'lang_de',
    'gl': 'DE'
}

response = requests.get(url, params=params)
results = response.json()['items']

for item in results:
    print(item['link'])

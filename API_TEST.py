import requests
import os

API_KEY = os.environ.get('BING_API_KEY')

headers = {
    'Ocp-Apim-Subscription-Key': API_KEY,
}

params = (
    ('q', 'superintendent Alabama'),
    ('count', '10'),
)

response = requests.get('https://api.bing.microsoft.com/v7.0/news/search', headers=headers, params=params)

print(response.json())
import requests
import os
from relevancy_check import RelevancyCheck
import time

class BingNewsSearch:
    BING_ENDPOINT = "https://api.bing.microsoft.com/v7.0/news/search"
    
    @classmethod
    def get_news_url(cls, state, count=5):
        base_url = "https://api.bing.microsoft.com/v7.0/news/search"
        
        # Prepare the query
        query_terms = [
            "superintendent resigns",
            "superintendent steps down",
            "superintendent departure",
            "superintendent leaves",
            "superintendent fired",
            "superintendent hired",
            "superintendent appointed",
            "superintendent retirement",
        ]
        query = f"({' OR '.join(query_terms)}) {state} -college"
        
        headers = {
            'Ocp-Apim-Subscription-Key': os.environ.get("BING_API_KEY")
        }
        
        params = {
            'q': query,
            'count': count,
            'mkt': 'en-US',
            'safeSearch': 'Off',
            'textFormat': 'HTML'
        }
        
        response = requests.get(base_url, headers=headers, params=params)
        time.sleep(1)
        data = response.json()
        
        if "value" not in data:
            print(f"No URLs returned from Bing for {state}.")
            return []
        
        urls = [item['url'] for item in data['value']]
        
        return urls

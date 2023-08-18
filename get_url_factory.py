import requests

class BingNewsSearch:

    BASE_URL = "https://api.bing.microsoft.com/v7.0/news/search"
    HEADERS = {
        "Ocp-Apim-Subscription-Key": "09a7a538f34f4f28bc029de2cd68248f"
    }

    @classmethod
    def get_news_urls(cls, query, count=10):
        params = {
            "q": query,
            "count": count,
            "textDecorations": True,
            "textFormat": "HTML"
        }

        response = requests.get(cls.BASE_URL, headers=cls.HEADERS, params=params)
        response.raise_for_status()

        data = response.json()
        urls = [value['url'] for value in data['value']]
        return urls

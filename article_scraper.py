import requests
from time import sleep

class ArticleScraper:
    def __init__(self, article_url):
        self.article_url = article_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def get_raw_data(self):
        try:
            response = requests.get(self.article_url, headers=self.headers, timeout=5)
            response.raise_for_status()
            if "text/html" in response.headers.get("content-type", ""):
             return response.text
            else:
                print(f"Failed to retrieve content from {self.article_url}. Invalid content type.")
                return None
        except requests.RequestException as e:
            print(f"Failed to retrieve content from {self.article_url}. Error: {e}")
            return None


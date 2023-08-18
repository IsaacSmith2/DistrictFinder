import time
from relevancy_check import RelevancyCheck
from article_scraper import ArticleScraper
from formater import Formatter
from district_inspector import DistrictInspector
from get_url_factory import BingNewsSearch

def main():
    processed_urls = set()
    query = "superintendent resigns OR superintendent steps down OR superintendent departure OR superintendent leaves -college"
    
    # Fetch URLs from Bing News Search
    urls = BingNewsSearch.get_news_urls(query, count=10)
    
    for article_url in urls:
        print(f"Processing article URL: {article_url}")
        if article_url in processed_urls:
            print(f"URL {article_url} has already been processed. Skipping.")
            continue
        
        # This is a simulated delay to prevent overloading the server. You can adjust the time as required.
        time.sleep(2)

        try:
            scraper = ArticleScraper(article_url)
            raw_html = scraper.get_raw_data()
            
            formatter = Formatter(raw_html)
            formatted_article = formatter.format_content()

            if not RelevancyCheck.check_relevancy(formatted_article):
                print(f"Article from URL: {article_url} is not relevant. Skipping.")
                continue

            inspector = DistrictInspector(formatted_article)
            district_name = inspector.get_district_name()

            print(f"District Name: {district_name}")
            
            processed_urls.add(article_url)

        except Exception as e:
            print(f"Error processing article {article_url}. Error: {e}")

if __name__ == "__main__":
    main()

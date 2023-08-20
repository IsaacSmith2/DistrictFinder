import os
from get_url_factory import BingNewsSearch
from article_scraper import ArticleScraper
from formater import Formatter
from relevancy_check import RelevancyCheck
from district_inspector import DistrictInspector
from url_history import URLHistory

def main():
    # List of states
    states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
              "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
              "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
              "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
              "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
              "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
              "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
              "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    
    # Looping through states and searching articles
    for state in states:
        print(f"\nSearching articles for {state}...")
        urls = BingNewsSearch.get_news_url(state)
        
        for url in urls:
            print(f"Processing article URL: {url}")
            
            # Check if URL has been processed before
            if URLHistory.check_and_add(url):
                print(f"URL {url} has already been processed. Skipping.")
                continue
            
            scraper = ArticleScraper(url)
            raw_html = scraper.get_raw_data()
            
            # Format the article content
            formatter = Formatter(raw_html)
            formatted_article = formatter.format_content()
            
            # Extract district name
            inspector = DistrictInspector(formatted_article)
            district_name = inspector.get_district_name()
            
            print(f"Found district: {district_name}")
            


if __name__ == "__main__":
    main()

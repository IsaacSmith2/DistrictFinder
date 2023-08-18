# formatter.py

from bs4 import BeautifulSoup

class Formatter:
    def __init__(self, raw_html):
        self.raw_html = raw_html

    def format_content(self):
        soup = BeautifulSoup(self.raw_html, 'html.parser')

        # Remove all script and style elements
        for script in soup(["script", "style"]):
            script.extract()

        # Get text
        text = soup.get_text()

        # Break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())

        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

        # Drop blank lines and join the chunks
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text
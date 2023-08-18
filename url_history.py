class URLHistory:
    def __init__(self, history_file='url_history.txt'):
        self.history_file = history_file
        self.processed_urls = self._load_history()

    def _load_history(self):
        try:
            with open(self.history_file, 'r') as f:
                return set(f.read().splitlines())
        except FileNotFoundError:
            return set()

    def save(self):
        with open(self.history_file, 'w') as f:
            for url in self.processed_urls:
                f.write(f"{url}\n")

    def check_and_add(self, url):
        """
        Checks if a URL has been processed. If not, adds it to the set.
        :param url: The URL to check and add.
        :return: True if the URL is new and hasn't been processed, False otherwise.
        """
        if url in self.processed_urls:
            return False
        else:
            self.processed_urls.add(url)
            self.save()
            return True

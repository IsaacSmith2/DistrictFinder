class URLHistory:
    _instance = None  # Class-level attribute to hold the single instance of URLHistory

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(URLHistory, cls).__new__(cls)
        return cls._instance

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

    @classmethod
    def check_and_add(cls, url):
        """
        Checks if a URL has been processed. If not, adds it to the set.
        :param url: The URL to check and add.
        :return: True if the URL is new and hasn't been processed, False otherwise.
        """
        instance = cls()
        if url in instance.processed_urls:
            return True
        else:
            instance.processed_urls.add(url)
            instance.save()
            return False
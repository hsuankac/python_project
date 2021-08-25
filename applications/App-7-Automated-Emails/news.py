import requests


class NewsFeed:
    """Representing multiple news titles and links as single string"""
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "14be30b5439547e4b821bef695251f2b"

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()
        articles = self._get_articles(url)
        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        res = requests.get(url)
        content = res.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apikey={self.api_key}"
        return url


if __name__ == '__main__':
    news = NewsFeed(interest='nasa', from_date='2021-08-23', to_date='2021-08-24', language='en')
    print(news.get())

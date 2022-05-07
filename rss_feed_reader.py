from bs4 import BeautifulSoup
import requests
from pyfiglet import figlet_format
import warnings


warnings.filterwarnings("ignore")


class Item(object):
    def __init__(self, _title: str, _link: str, _pub_date: str):
        self.title = _title
        self.link = _link
        self.pub_date = _pub_date

    def __str__(self):
        return "\u001b[36mtitle: " + self.title + "\n" + "link: " + self.link + "\n" + "pubDate: " + self.pub_date + "\n"


class RSSFeedReader(object):
    def __init__(self, _feed_links: list):
        self.feed_links = _feed_links

    def get_feeds(self) -> list:
        feeds = []
        for feed_link in self.feed_links:
            feed = requests.get(feed_link).text
            soup = BeautifulSoup(feed, "lxml")
            items = soup.findAll("item")

            for item in items:
                item = Item(item.title.text, item.guid.text, item.pubdate.text)
                feeds.append(item)

        return feeds


if __name__ == "__main__":
    print("\u001b[32m" + figlet_format("RSS FEED Reader", font="standard"))
    feed_links = ["https://techcentral.co.za/feed", "https://ventureburn.com/feed"]
    rss_feed = RSSFeedReader(feed_links)
    news_stories = rss_feed.get_feeds()

    for story in news_stories:
        print(story.__str__())

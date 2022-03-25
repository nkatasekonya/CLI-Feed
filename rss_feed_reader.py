#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests


class Item(object):
    def __init__(self, _title: str, _link: str, _pub_date: str, _description: str):
        self.title = _title
        self.link = _link
        self.pub_date = _pub_date
        self.description = _description

    def __str__(self):
        return "title: " + self.title + "\n" + "link: " + self.link + "\n" + "pubDate: " + self.pub_date + "\n" + "description: " + self.description + "\n"
        


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
                item = Item(item.title.text, item.guid.text, item.pubdate.text, item.description.text[9:-3])
                feeds.append(item)

        return feeds


if __name__ == "__main__":
    feed_links = ["https://techcentral.co.za/feed", "https://ventureburn.com/feed"]
    rss_feed = RSSFeedReader(feed_links)
    news_stories = rss_feed.get_feeds()

    for story in news_stories:
        print(story.__str__())

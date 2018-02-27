# -*- coding: utf-8 -*-

import requests
import urllib
from bs4 import BeautifulSoup
from youtubeitem import YouTubeItem

class YouTubeParser:

    webpage = "http://www.youtube.com"

    def __init__(self):
        pass

    def __getSearchPage(self, strSearch):
        dicSearch = {"search_query" : strSearch}
        encodedUrl = urllib.urlencode(dicSearch)
        url = self.webpage + "/results?" + encodedUrl
        page = requests.get(url)
        return page

    def search(self, strSearch):
        page = self.__getSearchPage(strSearch)
        items = []

        if (page.status_code == 200):
            soup = BeautifulSoup(page.content, 'html.parser')

            for h in soup.find_all("h3", class_="yt-lockup-title"):
                a = h.find("a")
                if a:
                    link = self.webpage + a.get("href")
                    print a.text + " " + link

        return page.content
# -*- coding: utf-8 -*-

from youtubeparser import YouTubeParser

def start():
    youtube = YouTubeParser();
    page = youtube.search("jason mraz")
    #print page

if __name__ == '__main__':
    start()


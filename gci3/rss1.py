#coding: utf8
import feedparser

RSS_URL = "http://news.yahoo.co.jp/pickup/rss.xml"

yahoo_news_dic = feedparser.parse(RSS_URL)

print yahoo_news_dic.feed.title

for entry in yahoo_news_dic.entries:
  title = entry.title
  link  = entry.link
  print link
  print title
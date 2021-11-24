import requests
from bs4 import BeautifulSoup
import re
import json
import grequests

r = requests.get('http://ac.hkie.org.hk/')
urls = []
divisonIDs = []
divisonNames = []
rss = []

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    a_tag = soup.find_all(href=re.compile("http"), class_="a1")
    # print(a_tag)
    # a_href_tag = a_tag.find("a")
    # print(a_href_tag)
    for tag in a_tag:
        # print(tag.get('href'))
        urls.append(tag.get('href'))
    for x in range(0,len(urls)):
        if urls[x][-1]!="/":
            urls[x] += "/"
        urls[x]= urls[x] + "en_Events_Up_Item.aspx"
    # print(urls)
    b_tag = soup.find(id="divMenuTest").find_all("a")
        # print(tag.string)
    for tag in b_tag :
        divisonNames.append(tag.string)
    # for URL in urls:
    #     r = requests.get(URL)
    #     soup = BeautifulSoup(r.text, 'html.parser')
    #     print(soup)
    rs = (grequests.get(u) for u in urls)
    results = grequests.map(rs)
    for result in results:
        if result != None:
            rss.append(BeautifulSoup(result.text, 'html.parser').find("form"))
    print (rss)

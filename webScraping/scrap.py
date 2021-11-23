import requests
from bs4 import BeautifulSoup
import re
import json

r = requests.get('http://ac.hkie.org.hk/')
URLs = []
divisonIDs = []
divisonNames = []
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    a_tag = soup.find_all(href=re.compile("http"), class_="a1")
    # print(a_tag)
    # a_href_tag = a_tag.find("a")
    # print(a_href_tag)
    for tag in a_tag:
        # print(tag.get('href'))
        URLs.append(tag.get('href'))
    for x in range(0,len(URLs)):
        if URLs[x][-1]!="/":
            URLs[x] += "/"
        URLs[x]= URLs[x] + "en_Events_Up.aspx?TypeSql=&&TypeName=Events+%2f+Activities"

    print(URLs)
    b_tag = soup.find(id="divMenuTest").find_all("a")
    for tag in b_tag:
        # print(tag.string)
        divisonNames.append(tag.string)
    # print(divisonNames)
# def func(x):
#     return x + 1
#
#
# def test_answer():
#     assert func(3) == 5

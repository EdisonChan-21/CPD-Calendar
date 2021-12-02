import requests
from bs4 import BeautifulSoup
import urllib
import re
import json

from spider import spider
from division import Division
from event import Event

divisionObjArr = []
eventAppendix = "en_Events_Up_Item.aspx"

def divisionInit():
    divisionPageUrl = "https://hkie.org.hk/membership/division/"
    request = spider.getRequest(divisionPageUrl)
    divisionName, divisionUrl = spider.getDivisionList(request)
    for name, url in zip(divisionName, divisionUrl):
        divisionObjArr.append(Division(name, url))
    if (divisionObjArr):
        for division in divisionObjArr:
            # print(obj.getDivisionDict())
            pass
    return True

def singleDivisionInit():
    divisionObjArr.append(Division("EL", "http://el.hkie.org.hk/en_Events_Up_Item.aspx", Event("go to school", "01/01/2021", "general")))
    # divisionObjArr.append(Division("EL", "http://el.hkie.org.hk/en_Events_Up_Item.aspx"))
    divisionObjArr.append(Division("AC", "http://ac.hkie.org.hk/en_Events_Up_Item.aspx"))
    return True

def saveJson(divisionObjArr):
    # Serializing json
    json_string = json.dumps([obj.getDivisionDict() for obj in divisionObjArr], indent = 4)

    # print (json_string)
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_string)

if(divisionInit()):
    # divisionObjArr = divisionObjArr[:10]
    for division in divisionObjArr:
        url = division.getUrl()
        if (url.find("hkie.org.hk") != -1) and (url.find("cdrc") == -1):
            request = spider.getRequest(url+eventAppendix)
            eventObjArr = spider.getEventsList(request)
            division.setEvent(eventObjArr)
            # for event in division.getEvent():
                # print (event.getDate())
                # print (event.getEventDict())
    saveJson(divisionObjArr)

# if(singleDivisionInit()):
#     saveJson(divisionObjArr)

import requests
from bs4 import BeautifulSoup
import urllib
import re

from concurrent.futures import ThreadPoolExecutor

from event import Event

class Spider:
    def __init__(self):
        self.eventAppendix = "en_Events_Up_Item.aspx"

    def getRequest(self,url):
        try:
            r = requests.get(url)
        except Exception as err:
            print(f'Error occurred: {err}')
            sys.exit()
        else:
            assert r.status_code == 200
            return r

    def getDivisionList(self,r):
        dvisionNameArr = []
        divisionUrlArr = []
        soup = BeautifulSoup(r.text, 'html.parser')
        tag = soup.find(class_="editor").find_all("a")
        for t in tag :
            dvisionNameArr.append(t.string.split(" (")[0])
            divisionUrlArr.append(t.get('href'))
        for i in range(0,len(divisionUrlArr)):
            if divisionUrlArr[i][-1]!="/":
                divisionUrlArr[i] += "/"
        return dvisionNameArr, divisionUrlArr

    def aspxRequest(self, r, pageNumber):
        if r.status_code == requests.codes.ok:
            key = "16"
            if (pageNumber >= 10):
                key = "17"
            soup = BeautifulSoup(r.text, 'html.parser')
            VIEWSTATE = soup.find(id="__VIEWSTATE")['value']
            VIEWSTATEGENERATOR = soup.find(id="__VIEWSTATEGENERATOR")['value']
            EVENTVALIDATION = soup.find(id="__EVENTVALIDATION")['value']

            header = {
                "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh;q=0.6",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
            }

            body = {
                "__VIEWSTATE":urllib.parse.quote_plus(VIEWSTATE),
                "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
                "__EVENTTARGET": "",
                "__EVENTARGUMENT": "",
                "Grid%24DXSelInput": "",
                "hf_SubMenuID": "",
                "hf_ISeq": "",
                "__CALLBACKID": "Grid",
                "__CALLBACKPARAM": "GB%7C"+ key +"%3BPAGERONCLICK%7CPN"+str(pageNumber)+"%3B",
                "__EVENTVALIDATION": urllib.parse.quote_plus(EVENTVALIDATION)
            }

            payload=""

            for key, value in body.items():
                payload = payload + key + "=" + value + "&"

            session = requests.Session()

            response = session.post(url=r.url, headers=header, data=payload[:-1])

            print("Page " + str(pageNumber+1) + " post request done")
            return response

    def getEventsList(self, r): #return a list of event object for each division
        if(r):
            eventObjArr = []
            soup = BeautifulSoup(r.text, 'html.parser')
            pageNumber = int(soup.find("td", {"class":"dxpSummary_BlackGlass"}).string.split('of ')[-1].split(' (')[0])
            print("Number of page : " + str(pageNumber) + " for URL : " + r.url)

            #shorter test time
            # if(pageNumber>=10):
            #     pageNumber = 5

            list_of_urls = [r]*pageNumber
            list_of_page = [i for i in range(0, pageNumber)]
            with ThreadPoolExecutor(max_workers=10) as pool:
                response_list = list(pool.map(self.aspxRequest, list_of_urls, list_of_page))

            for response in response_list:
                eventObjArr.extend(self.getEventTable(response))
            # for i in range(0, pageNumber):
            #     soup = BeautifulSoup(r.text, 'html.parser')
            #     response = self.aspxRequest(r, i)
            #     print("Page " + str(i+1) + " response:" + str(response))
            #     eventObjArr.extend(self.getEventTable(response))
            return eventObjArr

            # d = spider.toDict(r)
    def getEventTable(self, r): # return a list of event object for each event page`
        if(r):
            soup = BeautifulSoup(r.text, 'html.parser')
            table = soup.find("table" ,id="Grid_DXMainTable")
            eventTable = soup.findAll("td", id=re.compile("Grid_tccell.*"))
            eventObjArr = self.getEvent(r, eventTable)
            return eventObjArr

    def getEvent(self, r, eventTable):
        eventObjArr = []
        if(r):
            soup = BeautifulSoup(r.text, 'html.parser')
            table = soup.find("table" ,id="Grid_DXMainTable")
            eventTable = soup.findAll("td", id=re.compile("Grid_tccell.*"))
            eventDate = ""
            eventType = ""
            eventName = ""
            eventUrl = ""

            for e in eventTable:
                if(re.match('.*_0', e.get('id'))):
                    if (e.string is not None):
                        eventDate = e.string.strip()
                elif(re.match('.*_1', e.get('id'))):
                    if (e.string is not None):
                        eventType = e.string.strip()
                else:
                    if(e.find('a') is not None):
                        eventName = e.find('a').string
                        eventUrl = e.find('a').get('href')
                    else:
                        eventName = e.find('span').string
                if (eventDate and eventType and eventName):
                    eventObjArr.append(Event(eventName, eventDate, eventType, eventUrl))
                    eventDate = ""
                    eventType = ""
                    eventName = ""
                    eventUrl = ""
        return eventObjArr

spider = Spider()

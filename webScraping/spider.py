import requests
from bs4 import BeautifulSoup
import urllib
# import grequests

mainPageUrl = "https://hkie.org.hk/"
divisionAppendix = "membership/division/"
eventAppendix = "en_Events_Up_Item.aspx"

def getAllInfo():
    pass

def getRequest(url):
    r = requests.get(url)
    return r

def getDivisionName(r):
    divisonName = []
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        tag = soup.find(class_="editor").find_all("a")
        for t in tag :
            divisonName.append(t.string.split(" (")[0])
        return divisonName
    else:
        return -1

def getDivisionUrl(r):
    divisionUrl = []
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        tag = soup.find(class_="editor").find_all("a")
        for t in tag:
            divisionUrl.append(t.get('href'))
        for x in range(0,len(divisionUrl)):
            if divisionUrl[x][-1]!="/":
                divisionUrl[x] += "/"
            # urls[x]= urls[x] + "en_Events_Up_Item.aspx"
        return divisionUrl
    else:
        return -1

def mapping(name, url):
    dicts = []
    for i in range(0, len(name)):
        dicts.append({"divisionName": name[i], "divisionUrl": url[i]})
    return dicts

def aspxRequest(r):
    if r.status_code == requests.codes.ok:
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
            "__CALLBACKPARAM": "GB%7C16%3BPAGERONCLICK%7CPN60%3B",
            "__EVENTVALIDATION": urllib.parse.quote_plus(EVENTVALIDATION)
        }

        payload=""

        for key, value in body.items():
            payload = payload + key + "=" + value + "&"

        session = requests.Session()

        response = session.post(url=r.url, headers=header, data=payload[:-1])
        if response.status_code == requests.codes.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find("table" ,id="Grid_DXMainTable")
            return table


# print (getDivisionName(getResponse(mainPageUrl+divisionAppendix)))
# urlList = getDivisionUrl(getRequest(mainPageUrl+divisionAppendix))
# print (urlList)
# rs = (grequests.get(u) for u in urlList)
# results = grequests.map(rs)
# for result in results:
#     if result != None:
#         print(result.text)
r = getRequest(mainPageUrl+divisionAppendix)
dict = mapping(getDivisionName(r),getDivisionUrl(r))

for d in dict:
    if (d["divisionUrl"].find("hkie.org.hk") != -1) and (d["divisionUrl"].find("cdrc") == -1):
        resp = aspxRequest(getRequest(d["divisionUrl"]+eventAppendix))
        print(d["divisionUrl"]+eventAppendix)
    else:
        print ("URL : " + d["divisionUrl"] +" not suit for scrapping")

# print(dict[0]["divisionUrl"])

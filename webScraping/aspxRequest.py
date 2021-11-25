import requests
from bs4 import BeautifulSoup
import urllib

url = "http://ymc.hkie.org.hk/en_Events_Up_Item.aspx"

r = requests.get('http://ymc.hkie.org.hk/en_Events_Up_Item.aspx')

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

response = session.post(url=url, headers=header, data=payload[:-1])
print(response)
if response.status_code == requests.codes.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find("table" ,id="Grid_DXMainTable")
    print(table)
# if (body3 == body2):
    # print("match")

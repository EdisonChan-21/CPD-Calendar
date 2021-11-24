import requests
from bs4 import BeautifulSoup

url = "http://ac.hkie.org.hk/en_Events_Up_Item.aspx"

r = requests.get('http://ac.hkie.org.hk/en_Events_Up_Item.aspx')

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    VIEWSTATE = soup.find(id="__VIEWSTATE")['value']
    VIEWSTATEGENERATOR = soup.find(id="__VIEWSTATEGENERATOR")['value']
    EVENTVALIDATION = soup.find(id="__EVENTVALIDATION")['value']

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh;q=0.6"
    # "cookies": "_ga=GA1.3.819409100.1637641749; _gid=GA1.3.792281525.1637738437"
}

body = {
    "__VIEWSTATE":VIEWSTATE,
    "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "Grid%24DXSelInput": "",
    "Grid%24CallbackState":"%2FwEWBB4ERGF0YQXoEUFBQUFBRXdBQUFBQUFBQUFEd0FBQUFBREFBQUFDa1YyWlc1MFgwUmhkR1VLUlhabGJuUmZSR0YwWlFnQUFBeEZkbVZ1ZEY5T1lXMWxYMFVNUlhabGJuUmZUbUZ0WlY5RkJ3QUFDRlI1Y0dWT1lXMWxDRlI1Y0dWT1lXMWxCd0FBR3dBQUFBaEZkbVZ1ZEY5SlJBMUZkbVZ1ZEY5V1pXNTFaVjlGRFVWMlpXNTBYMVpsYm5WbFgwTU1SWFpsYm5SZlRtRnRaVjlERDBWMlpXNTBYME52Ym5SbGJuUmZSUTlGZG1WdWRGOURiMjUwWlc1MFgwTU9SWFpsYm5SZlJtbHNaWE5mUlRFT1JYWmxiblJmUm1sc1pYTmZRekVPUlhabGJuUmZSbWxzWlhOZlJUSU9SWFpsYm5SZlJtbHNaWE5mUXpJT1JYWmxiblJmUm1sc1pYTmZSVE1PUlhabGJuUmZSbWxzWlhOZlF6TU9SWFpsYm5SZlVtVndiM0owWDBVT1JYWmxiblJmVW1Wd2IzSjBYME1LU1hOZlJXNWhZbXhsWkFaRGNuUmZRbmtIUTNKMFgwUjBaUWxWY0dSaGRHVmZRbmtLVlhCa1lYUmxYMFIwWlFkRGIyNTBZV04wQlVWdFlXbHNBMVJsYkFkUVlYbHRaVzUwQkZScGJXVUVWSGx3WlF4cGMwVnVjbTlzYkcxbGJuUU1hWE5XYVdWM1JHVjBZV2xzQndBSEFBY0FCd0FHLy84Q0JBQ0FORmJ3Nzg4SUFoVlVaV05vYm1sallXd2dWbWx6YVhRZ0xTQkhSbE1DRDFSbFkyaHVhV05oYkNCV2FYTnBkQWNBQndBRy8vOENCQUFBcjFTbjlNOElBazVEVUVRZ1RHVmpkSFZ5WlNCdmJpQlRZV1psZEhrZ1RXRnVZV2RsYldWdWRDQlRlWE4wWlcwZzRvQ1RJSFJsZUhScGJtY2diM1YwSUhkaGVTQjBieUJoZG1saGRHbHZiaUJ6WVdabGRIa0NDME5RUkNCTVpXTjBkWEpsQndBSEFBYi8vd0lFQUFEbm9jd04wQWdDSjBOUVJDQk1aV04wZFhKbElHOXVJRlpwWW5KaGRHbHZiaUJwYmlCSVpXeHBZMjl3ZEdWeWN3SUxRMUJFSUV4bFkzUjFjbVVIQUFjQUJ2Ly9BZ1FBZ0dHZ2d4TFFDQUlwUVdseVkzSmhablFnUkdsMmFYTnBiMjRnUVVkTklFeGxZM1IxY21VZ1JHbHVibVZ5SURJd01UTUNBMEZIVFFjQUJ3QUcvLzhDQkFBQUgrL3hKdEFJQWtSRFVFUWdUR1ZqZEhWeVpTQmhibVFnVkdWamFHNXBZMkZzSUhacGMybDBJT0tBa3lCSGIzWmxjbTV0Wlc1MElFWnNlV2x1WnlCVFpYSjJhV05sY3lBb1IwWlRLUUlQVkdWamFHNXBZMkZzSUZacGMybDBCd0FIQUFiLy93SUVBRUJwN1hXdzBBZ0NRRlJsWTJodWFXTmhiQ0JXYVhOcGRDQXRJRWh2Ym1jZ1MyOXVaeUJCWlhKdklFVnVaMmx1WlNCVFpYSjJhV05sY3lCTWFXMXBkR1ZrSUNoSVFVVlRUQ2tDRDFSbFkyaHVhV05oYkNCV2FYTnBkQWNBQndBRy8vOENCQURBaXBWUnVOQUlBajlVWldOb2JtbGpZV3dnVEdWamRIVnlaU0RpZ0pNZ1JtOXliV0YwYVc5dUlHOW1JRUZwY21OeVlXWjBJRTFoYVc1MFpXNWhibU5sSUZCeWIyZHlZVzBDQzBOUVJDQk1aV04wZFhKbEJ3QUhBQWIvL3dJRUFFRDZrSGJHMEFnQ0wxUmxZMmh1YVdOaGJDQldhWE5wZENCMGJ5QklRVVZEVHlCdFlXbHVkR1Z1WVc1alpTQm1ZV05wYkdsMGFXVnpBZzlVWldOb2JtbGpZV3dnVm1semFYUUhBQWNBQnYvL0FnUUF3T1FwZVAzUUNBSXZWR1ZqYUc1cFkyRnNJRlpwYzJsMElIUnZJRU5NVUNCT2RXTnNaV0Z5SUZKbGMyOTFjbU5sY3lCRFpXNTBjbVVDRDFSbFkyaHVhV05oYkNCV2FYTnBkQWNBQndBRy8vOENCQURBVTRaMzU5QUlBaDVFYVhOamIzWmxjaUJCZG1saGRHbHZiaUJEWVhKbFpYSnpJREl3TVRRQ0IwZGxibVZ5WVd3SEFBY0FCdi8vQWdRQUFFVXVJSFRSQ0FKV1ZHVmphRzVwWTJGc0lGTmxiV2x1WVhJNklGTjBjblZqZEhWeVlXd2dTVzUwWldkeWFYUjVMQ0JTWld4cFlXSnBiR2wwZVNCaGJtUWdVMkZtWlhSNUlHOW1JRWRoY3lCVWRYSmlhVzVsSUVWdVoybHVaWE1DQzBOUVJDQk1aV04wZFhKbEJ3QUhBQWIvL3dJRUFFQ0Q2OGErMFFnQ1VGUmxZMmh1YVdOaGJDQldhWE5wZENCMGJ5QkJWa2xESUZocDRvQ1pZVzRnUVdseVkzSmhablFnU1c1a2RYTjBjbmtnS0VkeWIzVndLU0JEYjIxd1lXNTVJRXgwWkNBb1FWWkpReUJZUVVNcEFnOVVaV05vYm1sallXd2dWbWx6YVhRSEFBY0FCdi8vQWdRQUFGRnYvYkxSQ0FJNlZHVmphRzVwWTJGc0lGWnBjMmwwSU9LQWt5QkliMjVuSUV0dmJtY2dRV1Z5YnlCRmJtZHBibVVnVTJWeWRtbGpaWE1nS0VoQlJWTk1LUUlQVkdWamFHNXBZMkZzSUZacGMybDBCd0FIQUFiLy93SUVBQUQ0R0NLMjBRZ0NHa2hMU1VVZ1FVVkVVeUJTWldOeWRXbDBiV1Z1ZENCVVlXeHJBZ2RIWlc1bGNtRnNCd0FIQUFiLy93SUVBSUE3Q1AvcDBRZ0NNbFJsWTJodWFXTmhiQ0JXYVhOcGRDQjBieUJIYjNabGNtNXRaVzUwSUVac2VXbHVaeUJUWlhKMmFXTmxJQ2hIUmxNcEFnOVVaV05vYm1sallXd2dWbWx6YVhRPR4FU3RhdGUFQEJ3TUhBQUlCQndFQ0FRY0NBZ0VIQUFjQUJ3QUNBQWIvL3drQ0FBa0NBQUlBQXdjRUFnQUhBQUlCQndBQ0FRY0E%3D",
    "hf_SubMenuID": "",
    "hf_ISeq": "",
    "__CALLBACKID": "Grid",
    "__CALLBACKPARAM": "GB%7C16%3BPAGERONCLICK%7CPB2%3B",
    "__EVENTVALIDATION": EVENTVALIDATION

}

session = requests.Session()
# response = session.get(validation_url, params=payload)

# soup = BeautifulSoup(response.content)
# callbackid = soup.select('input[name=__CALLBACKID]')[0]['value']

response = session.post(url=url, data = body, headers=header)
if response.status_code == requests.codes.ok:
    print (BeautifulSoup(response.text, 'html.parser'))

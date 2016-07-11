import requests

with requests.Session() as s:
    url_0 = "http://125.141.219.95/login.spw"
    USERNAME = 'nobody'
    PASSWORD = 'guests'
    s.get(url_0)
    jsseionid = s.cookies['JSESSIONID']
    payload = {
        "userId" : USERNAME,
        "userPassword" : PASSWORD,
        "JSESSIONID": jsseionid
    }

    s.post(url_0, data = payload, headers = dict(referer="http://125.141.219.95/"))

    page = s.get("http://125.141.219.95/projectInfo.spw?projectId=1")
    print(page.status_code)

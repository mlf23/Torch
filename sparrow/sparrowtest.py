import requests
import post
from urllib.parse import urlparse

url = 'http://125.141.219.95/login.spw'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)
print(response.cookies['JSESSIONID'])
print(response.content)
print(response.url[0])
USERNAME = 'guest1'
PASSWORD = 'guests'

payload = {
    "userId" : USERNAME,
    "userPassword" : PASSWORD,
    "JSESSIONID" : response.cookies['JSESSIONID']
}

print("----current status-----")
print(response.cookies['JSESSIONID'])
print(payload)
# print("Username : " + USERNAME)
# print("Password : " + PASSWORD)
print("\n\n")

response = requests.post('http://125.141.219.95/authenticate.spw', data = payload, headers = headers)

# nextUrl = response.url
# parsed = urlparse(nextUrl)
# print(response.url)
# print(parsed)
# print(parsed.params)
# print(parsed.params[11:])
# print("\n\nSucces parsing-----")
#
# login_jsessionid = parsed.params[11:]
# nextUrl = parsed.query[8:]
# print(nextUrl)
# print(login_jsessionid)
# print("\n\n")

# payload = {
#     "jsessionid" : login_jsessionid
#     # "nextUrl" :
# }

print("----------Here is after login requests-----------")
print(response.url)
print(response.content)
# print(response.content)

response = requests.get('http://125.141.219.95/projectList.spw', headers = headers)
print("----------Project Page!!!-----------")
# print(response.url)
# print(response.content)

print("----current status-----")
print(payload)
# print("Username : " + USERNAME)
# print("Password : " + PASSWORD)
print("\n\n")





print("Current Payload\n")
print(payload)
print("\n\n")

# 아마 포스트로 jsessionid 넘겨야 한다.
responese = requests.post('http://125.141.219.95/projectList.spw', data=payload, headers = headers)
print(response.url)
# print(response.cookies['JSESSIONID'])

# USERNAME = 'nobody'
# PASSWORD = 'guests'
#
# url_0 = "http://125.141.219.95/login.spw"
# USERNAME = 'nobody'
# PASSWORD = 'guests'
# s.get(url_0)
# jsseionid = s.cookies['JSESSIONID']
# payload = {
#     "userId" : USERNAME,
#     "userPassword" : PASSWORD,
#     "JSESSIONID": jsseionid
# }
#
# s.post(url_0, data = payload, headers = dict(referer="http://125.141.219.95/"))
#
# page = s.get("http://125.141.219.95/projectInfo.spw?projectId=1")
# print(page.status_code)

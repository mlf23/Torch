from django.shortcuts import render
import requests
# Create your views here.

def sendPacketToSparrow:
    url = 'http://125.141.219.95'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get(url, headers=headers)
    print(response.content)

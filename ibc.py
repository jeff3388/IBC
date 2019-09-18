from bs4 import BeautifulSoup
import requests

cert_file_path = "cert.pem"
key_file_path = "key.pem"
cert = (cert_file_path, key_file_path)

headers = {
    'Request URL': 'https://www.nova88.com/Default.aspx?IsSSL=1&hidSelLang=en',
    'Request Method': 'GET',
    'Remote Address': '142.44.161.141:8080',
    'Referrer Policy': 'no-referrer-when-downgrade',
    'Cache-Control': 'private',
    'Connection': 'keep-alive',
    'Content-Encoding': 'gzip',
    'Content-Type': 'text/html; charset=utf-8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Host': 'www.nova88.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
}

payload = {
    'IsSSL': '1',
    'hidSelLang': 'en'
}
########## proxy setting ###########

proxy = "142.44.161.141:8080"
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
####################################

url = 'https://www.nova88.com/Default.aspx?IsSSL=1&hidSelLang=en'

res = requests.get(url=url,headers=headers,proxies=proxies,params=payload,verify=False).content
soup = BeautifulSoup(res, 'html.parser')
titile = soup.find_all("div", attrs={"class": "lobby-title"})
for t in titile:
    t = t.text
    print(t)
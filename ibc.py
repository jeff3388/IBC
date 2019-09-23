from urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import requests
import warnings

headers = {
    'Host': 'www.nova88.com',
    'Remote Address': '159.203.15.11:22222',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br'
}

########## proxy setting ###########

proxy = "60.53.207.49:8080"
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
####################################

url = 'https://www.nova88.com/Default.aspx?IsSSL=1&hidSelLang=en'

warnings.simplefilter('ignore',InsecureRequestWarning)
res = requests.get(url=url,headers=headers,proxies=proxies,verify=False).content
soup = BeautifulSoup(res, 'html.parser')
titile = soup.find_all("div", attrs={"class": "lobby-title"})
for t in titile:
    t = t.text
    print(t)
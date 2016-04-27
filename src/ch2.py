from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

bsObj = BeautifulSoup(html.read(), "lxml") #这个地方第一个参数用html.read()也可以
nameList = bsObj.find_all("span", {"class":"green"})
for name in nameList:
    print(name.get_text())

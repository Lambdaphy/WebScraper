from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def get_links(path):
    html = urlopen("http://en.wikipedia.org" + path)
    bs_obj = BeautifulSoup(html.read(), "lxml")
    return bs_obj.find("div", {"id":"bodyContent"}).find_all("a", {"href":re.compile("^(/wiki/)((?!:).)*$")})


links = get_links("/wiki/Kevin_Bacon")
while len(links) > 0:
    new_article = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(new_article)
    links = get_links(new_article)
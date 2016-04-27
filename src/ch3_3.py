from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def get_links(pageURL):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageURL)
    bs_obj = BeautifulSoup(html, "lxml")
    for link in bs_obj.find_all("a", {"href":re.compile("^(/wiki/)")}):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                new_page = link.attrs["href"]
                print(new_page)
                pages.add(new_page)
                get_links(new_page)

get_links("")
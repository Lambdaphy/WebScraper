from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def get_links(page_url):
    global pages
    html = urlopen("http://en.wikipedia.org" + page_url)
    bs_obj = BeautifulSoup(html, "lxml")
    do_something(bs_obj)
    
    for link in bs_obj.find_all("a", {"href":re.compile("^(/wiki/)((?!:).)*$")}):
            if "href" in link.attrs:
                if link.attrs["href"] not in pages:
                    new_page = link.attrs["href"]
                    print("----------------------------------------\n" + new_page)
                    pages.add(new_page)
                    get_links(new_page)

def do_something(bs_obj):
    try:
        print("Title: " + bs_obj.h1.get_text())
        print("First Paragraph: " + bs_obj.find(id = "mw-content-text").find_all("p")[0].get_text())
        print("Edit Link: " + bs_obj.find(id = "ca-edit").find("span").find("a").attrs["href"])
    except AttributeError:
        print("This page is missing something!")

get_links("")
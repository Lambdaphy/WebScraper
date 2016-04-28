from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()

random.seed(datetime.datetime.now())

def get_internal_links(bs_obj, include_url):
    internal_links = []
    #Find all links that begin with a "/"
    for link in bs_obj.find_all("a", href = re.compile("^(/|.*"+include_url+")")):
        if link.attrs["href"] is not None and link.attrs["href"] not in internal_links:
            internal_links.append(link.attrs["href"])
    return internal_links


def get_external_links(bs_obj, exclude_url):
    external_links = []
    #Find all links that start with "http" or "www" that do not contain the current URL
    for link in bs_obj.find_all("a", href = re.compile("^(http|www)((?!"+exclude_url+").)*$")):
        if link.attrs["href"] is not None and link.attrs["href"] not in external_links:
            external_links.append(link.attrs["href"])
    return external_links


def split_address(address):
    address_parts = address.replace("http://", "").replace("https://", "").split("/")
    return address_parts


def get_random_external_link(starting_page):
    html = urlopen(starting_page)
    bs_obj = BeautifulSoup(html, "lxml")
    external_links = get_external_links(bs_obj, split_address(starting_page)[0])
    if len(external_links) == 0:
        internal_links = get_internal_links(bs_obj, split_address(starting_page)[0])
        return get_random_external_link(internal_links[random.randint(0, len(internal_links) - 1)])
    else:
        return external_links[random.randint(0, len(external_links) - 1)]

def follow_external_link_only(starting_page):
    external_link = get_random_external_link(starting_page)
    print("Random external link is: " + external_link)
    follow_external_link_only(external_link)

follow_external_link_only("https://www.hao123.com/")
        
            
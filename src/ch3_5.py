from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random



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

def get_all_external_links(site_url):
    html = urlopen(site_url)
    bs_obj = BeautifulSoup(html, "lxml")
    internal_links = get_internal_links(bs_obj, split_address(site_url)[0])
    external_links = get_external_links(bs_obj, split_address(site_url)[0])
    for link in external_links:
        if link not in all_external_links:
            all_external_links.add(link)
            print(link)
    for link in internal_links:
        if link not in all_internal_links:
            all_internal_links.add(link)
            get_all_external_links(link)
    
pages = set()
all_internal_links = set()
all_external_links = set()
random.seed(datetime.datetime.now())

#follow_external_link_only("http://www.163.com/")
get_all_external_links("http://www.163.com")      
            
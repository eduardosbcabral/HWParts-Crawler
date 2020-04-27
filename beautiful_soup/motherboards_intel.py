from bs4 import BeautifulSoup
import requests
from parser_bs import ParserBS
import time
import json

parser = ParserBS()

start_url = 'http://www.newegg.com/Intel-Motherboards/SubCategory/ID-280/Page-1?PageSize=96'

outputfilename = 'motherboards_intel.json'

components = []

def parse(url):

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    if parser.current_page == 1:
        parser.get_maximum_page(soup)

    for componentElement in parser.get_all_components(soup):
        component_url = parser.get_url_from_component(componentElement)
        component = parse_component(component_url)
        components.append(component)
        time.sleep(2.5)

    if parser.current_page <= parser.maximum_page:
        next_page_url = parser.get_next_page_url(url)
        parse(next_page_url)

def parse_component(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    return parser.get_all_specifications(soup, url)

try:
    parse(start_url)
finally:
    with open(outputfilename, 'w') as outfile:
        json.dump(components, outfile, indent=4, sort_keys=True)
import scrapy
from hwparts_crawler.services.parser import Parser

class NeweggamdmotherboardsSpider(scrapy.Spider):
    name = 'NewEggAMDMotherboards'
    allowed_domains = ['www.newegg.com']
    start_urls = [f'http://www.newegg.com/AMD-Motherboards/SubCategory/ID-22/Page-1?PageSize=96']
    parser = Parser()
    item_order = 1

    def parse(self, response):
        if self.parser.current_page == 1:
            # self.parser.get_maximum_page(response)
            self.parser.maximum_page = 5

        for component in self.parser.get_all_components(response):
            url = self.parser.get_url_from_component(component)
            yield response.follow(url, self.parse_component, meta={'item_order': self.item_order})
            self.item_order = self.item_order + 1

        if self.parser.current_page <= self.parser.maximum_page:
            next_page_url = self.parser.get_next_page_url(response)
            self.parser.next_page()
            print("========================================================================\n")
            print("Pagina atual: " + str(self.parser.current_page) + "\n")
            print("Proxima url: " + next_page_url + "\n")
            print("========================================================================\n")
            yield response.follow(next_page_url, self.parse)

    def parse_component(self, response):
        return self.parser.get_all_specifications(response, response.meta.get('item_order'))
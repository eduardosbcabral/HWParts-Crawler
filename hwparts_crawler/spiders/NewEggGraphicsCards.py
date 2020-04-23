import scrapy
from hwparts_crawler.services.parser import Parser

class NewegggraphicscardsSpider(scrapy.Spider):
    name = 'NewEggGraphicsCards'
    allowed_domains = ['www.newegg.com']
    start_urls = [f'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-1?PageSize=96']
    parser = Parser()

    def parse(self, response):
        if self.parser.current_page == 1:
            self.parser.get_maximum_page(response)

        for component in self.parser.get_all_components(response):
            url = self.parser.get_url_from_component(component)

            yield response.follow(url, self.parse_component)

        if self.parser.current_page <= self.parser.maximum_page:
            next_page_url = self.parser.get_next_page_url(response)
            self.parser.next_page()
            yield response.follow(next_page_url, self.parse)

    def parse_component(self, response):
        yield self.parser.get_all_specifications(response)

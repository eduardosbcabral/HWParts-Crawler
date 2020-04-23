from datetime import datetime

class Parser():

    item_order = 1
    current_page = 1

    def get_all_specifications(self, response):
        specification_elements = response.css('div#detailSpecContent div#Specs fieldset dl')

        specifications = dict()

        for element in specification_elements:
            obj = self.get_field_set_content(element)
            specifications.update(obj)

        specifications.update({
            'platform_id': self.get_platform_id(response),
            'image_url': self.get_image(response),
            'url': response.url,
            'platform': 'NewEgg',
            'item_order': self.item_order,
            'crawled_date': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

        self.item_order = self.item_order + 1

        return specifications

    def get_field_set_content(self, element):

        title = element.css('dt a::text').get(default='')

        if title == '':
            title = element.css('dt::text').get()
        
        content = element.css('dd::text').get()

        obj = dict()
            
        obj.update({
            title: content
        })
        return obj

    def find_element_content(self, response, element):
        specification_element = response.css('div#detailSpecContent div#Specs >fieldset')

        xpath_query_contains_anchor_tag = f'//dt[a[text()="{element}"]]'
        xpath_query = ''

        anchor_tag_element = specification_element.xpath(xpath_query_contains_anchor_tag).get(default='')
        if(anchor_tag_element == ''):
            xpath_query = f'//dt[text()="{element}"]/parent::dl//dd/text()'
        else:
            xpath_query = f'//dt[a[text()="{element}"]]/parent::dl//dd/text()'
            pass

        return specification_element.xpath(xpath_query).get(default='')

    def get_maximum_page(self, response):
        maximum_page = response.css('span.list-tool-pagination-text').xpath('//strong/text()').get().split('/')[1]
        self.maximum_page = int(maximum_page)
        return self.maximum_page

    def get_platform_id(self, response):
        return response.css('li.is-current').xpath('//em/text()').get()

    def get_image(self, response):
        return response.css('div.objImages span.mainSlide img').attrib['src']

    def get_all_components(self, response):
        return response.css('.items-view>.item-container:not(.is-feature-item)')

    def get_url_from_component(self, response):
        return response.css('a.item-title').xpath('@href').get()

    def get_next_page_url(self, response):
        next_page_url = response.url.replace(f'Page-{self.current_page}', f'Page-{self.current_page+1}')
        return next_page_url

    def next_page(self):
        self.current_page = self.current_page + 1
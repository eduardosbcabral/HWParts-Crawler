from datetime import datetime

class ParserBS():

    item_order = 1
    current_page = 1

    sequential_errors = 0

    def get_all_specifications(self, page, url):
        specification_elements = page.select('div#detailSpecContent div#Specs fieldset dl')

        specifications = dict()

        try:
            for element in specification_elements:
                obj = self.get_field_set_content(element)
                specifications.update(obj)

                specifications.update({
                    'platform_id': self.get_platform_id(url),
                    'images_urls': self.get_images(page),
                    'url': url,
                    'platform': 'NewEgg',
                    'item_order': self.item_order,
                    'crawled_date': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                })
        except:
            if self.sequential_errors < 10:
                self.sequential_errors = self.sequential_errors + 1
                print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
                print('Error when Crawling Component : ' + str(self.item_order-1))
                print('Component Url: ' + url)
                print('Component Current Page: ' + self.current_page)
                self.get_all_specifications(page, url)
            else:
                exit()

        if self.sequential_errors > 0:
            self.sequential_errors = 0

        print('======================================')
        print('Crawled Components: ' + str(self.item_order))

        self.item_order = self.item_order + 1

        return specifications

    def get_field_set_content(self, element):
        titleElement = element.select('dt a')

        title = ''

        if len(title) == 0:
            title = element.select('dt')[0].getText()
        else:
            title = titleElement[0].getText()

        content = element.select('dd')[0].getText()

        obj = dict()
            
        obj.update({
            title: content
        })
        return obj

    def get_maximum_page(self, page):
        maximum_page = page.select('span.list-tool-pagination-text strong')[0].text.split('/')[1]
        self.maximum_page = int(maximum_page)
        return self.maximum_page

    def get_platform_id(self, url):
        splitted = url.split('/')
        return splitted[len(splitted)-1]

    def get_images(self, response):
        images_elements = response.select('div.objImages ul.navThumbs img')
        images = []
        for image_element in images_elements:
            images.append(image_element.attrs['src'].replace('CompressAll35', ''))
        return images

    def get_all_components(self, response):
        components = response.select('.items-view>.item-container:not(.is-feature-item)')
        print('======================================')
        print('Page Components: ' + str(len(components)))
        return components

    def get_url_from_component(self, response):
        return response.select('a.item-title')[0].attrs['href']

    def get_next_page_url(self, url):
        next_page_url = url.replace(f'Page-{self.current_page}', f'Page-{self.current_page+1}')
        self.next_page(next_page_url)
        return next_page_url

    def next_page(self, next_page_url):
        self.current_page = self.current_page + 1
        print('######################################')
        print('######### Crawling Next Page: ' + str(self.current_page))
        print('######### Next Page Url: ' + next_page_url)
        print('######################################')
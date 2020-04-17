import scrapy
from hwparts_crawler.items import ProcessorsItem

class NeweggamdprocessorsSpider(scrapy.Spider):
    name = 'NewEggAMDProcessors'
    allowed_domains = ['www.newegg.com']
    current_page = 1
    processor_order = 1
    start_urls = [f'https://www.newegg.com/Processors-Desktops/SubCategory/ID-343/Page-{current_page}?PageSize=96']
    
    def parse(self, response):

        if self.current_page == 1:
            self.maximum_page = self.get_maximum_page(response)
        
        for processor in response.css('.items-view>.item-container:not(.is-feature-item)'):

            url = processor.css('a.item-title').xpath('@href').get()

            yield response.follow(url, self.parse_processor)

        if self.current_page <= self.maximum_page:
            next_page_url = response.url.replace(f'Page-{self.current_page}', f'Page-{self.current_page+1}')
            self.current_page = self.current_page + 1
            yield response.follow(next_page_url, self.parse)

    def parse_processor(self, response):
        # model
        brand = self.find_element_content(response, 'Brand')
        series = self.find_element_content(response, 'Series')
        name = self.find_element_content(response, 'Name')
        model = self.find_element_content(response, 'Model')

        # details
        cpu_socket_type = self.find_element_content(response, 'CPU Socket Type')
        core_name = self.find_element_content(response, 'Core Name')
        number_of_cores = self.find_element_content(response, '# of Cores')
        number_of_threads = self.find_element_content(response, '# of Threads')
        operating_frequency = self.find_element_content(response, 'Operating Frequency')
        max_turbo_frequency = self.find_element_content(response, 'Max Turbo Frequency')
        l3_cache = self.find_element_content(response, 'L3 Cache')
        manufacturing_tech = self.find_element_content(response, 'Manufacturing Tech')
        sixtyfour_bit_support = self.find_element_content(response, '64-Bit Support')
        hyper_threading_support = self.find_element_content(response, 'Hyper-Threading Support')
        memory_types = self.find_element_content(response, 'Memory Types')
        memory_channel = self.find_element_content(response, 'Memory Channel')
        virtualization_technology_support = self.find_element_content(response, 'Virtualization Technology Support')
        integrated_graphics = self.find_element_content(response, 'Integrated Graphics')
        graphics_base_frequency = self.find_element_content(response, 'Graphics Base Frequency')
        graphics_max_dynamic_frequency = self.find_element_content(response, 'Graphics Max Dynamic Frequency')
        pci_express_revision = self.find_element_content(response, 'PCI Express Revision')
        max_number_of_pci_express_lanes = self.find_element_content(response, 'Max Number of PCI Express Lanes')
        thermal_design_power = self.find_element_content(response, 'Thermal Design Power')
        cooling_device = self.find_element_content(response, 'Cooling Device')

        # informations
        platform_id = response.css('li.is-current').xpath('//em/text()').get()
        image_url = response.css('div.objImages span.mainSlide img').attrib['src']
        url = response.url
        platform = "NewEgg"

        processor = ProcessorsItem(
            brand = brand, 
            series = series,
            name = name,
            model = model,
            cpu_socket_type = cpu_socket_type,
            core_name = core_name,
            number_of_cores = number_of_cores,
            number_of_threads = number_of_threads,
            operating_frequency = operating_frequency,
            max_turbo_frequency = max_turbo_frequency,
            l3_cache = l3_cache,
            manufacturing_tech = manufacturing_tech,
            sixtyfour_bit_support = sixtyfour_bit_support,
            hyper_threading_support = hyper_threading_support,
            memory_types = memory_types,
            memory_channel = memory_channel,
            virtualization_technology_support = virtualization_technology_support,
            integrated_graphics = integrated_graphics,
            graphics_base_frequency = graphics_base_frequency,
            graphics_max_dynamic_frequency = graphics_max_dynamic_frequency,
            pci_express_revision = pci_express_revision,
            max_number_of_pci_express_lanes = max_number_of_pci_express_lanes,
            thermal_design_power = thermal_design_power,
            cooling_device = cooling_device,
            platform_id = platform_id,
            image_url = image_url,
            url = url,
            platform = platform,
            order = self.processor_order
        )

        self.processor_order = self.processor_order + 1

        yield processor

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
        return int(maximum_page)
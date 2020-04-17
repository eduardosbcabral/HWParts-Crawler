import scrapy
from hwparts_crawler.items import MotherboardsItem

class NeweggintelmotherboardsSpider(scrapy.Spider):
    name = 'NewEggINTELMotherboards'
    allowed_domains = ['www.newegg.com']
    current_page = 1
    motherboard_order = 1
    start_urls = [f'http://www.newegg.com/Intel-Motherboards/SubCategory/ID-280/Page-{current_page}?PageSize=96']
    
    def parse(self, response):

        if self.current_page == 1:
            self.maximum_page = self.get_maximum_page(response)
        
        for motherboard in response.css('.items-view>.item-container:not(.is-feature-item)'):

            url = motherboard.css('a.item-title').xpath('@href').get()

            yield response.follow(url, self.parse_motherboard)

        if self.current_page <= self.maximum_page:
            next_page_url = response.url.replace(f'Page-{self.current_page}', f'Page-{self.current_page+1}')
            self.current_page = self.current_page + 1
            yield response.follow(next_page_url, self.parse)

    def parse_motherboard(self, response):
        # model
        brand = self.find_element_content(response, 'Brand')
        series = self.find_element_content(response, 'Series')
        model = self.find_element_content(response, 'Model')

        # supported cpu
        cpu_socket_type = self.find_element_content(response, 'CPU Socket Type')
        cpu_type = self.find_element_content(response, 'CPU Type')

        # chipsets
        chipset = self.find_element_content(response, 'Chipset')

        # memory
        number_memory_slots = self.find_element_content(response, 'Number of Memory Slots')
        memory_standard = self.find_element_content(response, 'Memory Standard')
        maximum_memory = self.find_element_content(response, 'Maximum Memory Supported')
        channel_supported = self.find_element_content(response, 'Channel Supported')

        # storage devices
        sata_6 = self.find_element_content(response, 'SATA 6Gb/s')
        m2 = self.find_element_content(response, 'M.2')
        sata_raid = self.find_element_content(response, 'SATA RAID')

        # onboard video
        onboard_video_chipset = self.find_element_content(response, 'Onboard Video Chipset')

        # onboard audio
        audio_chipset = self.find_element_content(response, 'Audio Chipset')
        audio_channels = self.find_element_content(response, 'Audio Channels')

        # onboard lan
        lan_chipset = self.find_element_content(response, 'LAN Chipset')
        max_lan_speed = self.find_element_content(response, 'Max LAN Speed')
        wireless_lan = self.find_element_content(response, 'Wireless LAN')
        bluetooth = self.find_element_content(response, 'Bluetooth')

        # physical spec
        form_factor = self.find_element_content(response, 'Form Factor')
        led_lightning = self.find_element_content(response, 'LED Lighting')
        dimensions = self.find_element_content(response, 'Dimensions (W x L)')
        power_pin = self.find_element_content(response, 'Power Pin')

        # informations
        platform_id = response.css('li.is-current').xpath('//em/text()').get()
        motherboard_type = "AMD"
        image_url = response.css('div.objImages span.mainSlide img').attrib['src']
        url = response.url
        platform = "NewEgg"

        motherboard = MotherboardsItem(
            brand = brand, 
            series = series,
            model = model,
            cpu_socket_type = cpu_socket_type,
            cpu_type = cpu_type,
            chipset = chipset,
            number_memory_slots = number_memory_slots,
            memory_standard = memory_standard,
            maximum_memory = maximum_memory,
            channel_supported = channel_supported,
            sata_6 = sata_6,
            m2 = m2,
            sata_raid = sata_raid,
            onboard_video_chipset = onboard_video_chipset,
            audio_chipset = audio_chipset,
            audio_channels = audio_channels,
            lan_chipset = lan_chipset,
            max_lan_speed = max_lan_speed,
            wireless_lan = wireless_lan,
            bluetooth = bluetooth,
            form_factor = form_factor,
            led_lightning = led_lightning,
            dimensions = dimensions,
            power_pin = power_pin,
            platform_id = platform_id,
            motherboard_type = motherboard_type,
            image_url = image_url,
            url = url,
            platform = platform,
            order = self.motherboard_order
        )

        self.motherboard_order = self.motherboard_order + 1

        yield motherboard

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
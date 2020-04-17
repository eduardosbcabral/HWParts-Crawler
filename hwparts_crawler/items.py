# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MotherboardsItem(scrapy.Item):
    # model
    brand = scrapy.Field()
    series = scrapy.Field()
    model = scrapy.Field()
    
    # supported cpu
    cpu_socket_type = scrapy.Field()
    cpu_type = scrapy.Field()

    # chipsets
    chipset = scrapy.Field()

    # memory
    number_memory_slots = scrapy.Field()
    memory_standard = scrapy.Field()
    maximum_memory = scrapy.Field()
    channel_supported = scrapy.Field()

    # storage devices
    sata_6 = scrapy.Field()
    m2 = scrapy.Field()
    sata_raid = scrapy.Field()

    # onboard video
    onboard_video_chipset = scrapy.Field()

    # onboard audio
    audio_chipset = scrapy.Field()
    audio_channels = scrapy.Field()

    # onboard lan
    lan_chipset = scrapy.Field()
    max_lan_speed = scrapy.Field()
    wireless_lan = scrapy.Field()
    bluetooth = scrapy.Field()

    # physical spec
    form_factor = scrapy.Field()
    led_lightning = scrapy.Field()
    dimensions = scrapy.Field()
    power_pin = scrapy.Field()

    # informations
    platform_id = scrapy.Field()
    motherboard_type = scrapy.Field()
    image_url = scrapy.Field()
    url = scrapy.Field()
    platform = scrapy.Field()
    order = scrapy.Field()
    
    pass

class ProcessorsItem(scrapy.Item):

    # model
    brand = scrapy.Field()
    series = scrapy.Field()
    name = scrapy.Field()
    model = scrapy.Field()
    
    # details
    cpu_socket_type = scrapy.Field()
    core_name = scrapy.Field()
    number_of_cores = scrapy.Field()
    number_of_threads = scrapy.Field()
    operating_frequency = scrapy.Field()
    max_turbo_frequency = scrapy.Field()
    l3_cache = scrapy.Field()
    manufacturing_tech = scrapy.Field()
    sixtyfour_bit_support = scrapy.Field()
    hyper_threading_support = scrapy.Field()
    memory_types = scrapy.Field()
    memory_channel = scrapy.Field()
    virtualization_technology_support = scrapy.Field()
    integrated_graphics = scrapy.Field()
    graphics_base_frequency = scrapy.Field()
    graphics_max_dynamic_frequency = scrapy.Field()
    pci_express_revision = scrapy.Field()
    max_number_of_pci_express_lanes = scrapy.Field()
    thermal_design_power = scrapy.Field()
    cooling_device = scrapy.Field()

    # informations
    platform_id = scrapy.Field()
    image_url = scrapy.Field()
    url = scrapy.Field()
    platform = scrapy.Field()
    order = scrapy.Field()
    

    pass
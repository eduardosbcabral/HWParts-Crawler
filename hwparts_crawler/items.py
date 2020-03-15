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

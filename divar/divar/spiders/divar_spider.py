import json

import scrapy

url = 'https://divar.ir/v/-/{token}'

token_file = open('/home/amir/Desktop/proj/webScripting/tokens.txt', 'r', encoding='utf8')
tokens = token_file.read().split(',')
token_file.close()


class DivarSpider(scrapy.Spider):
    name = 'divar'
    start_urls = [url.format(token=token) for token in tokens]

    def parse(self, response):
        title = response.css('div div.kt-page-title__title--responsive-sized::text').extract()
        description = response.css('div div.kt-page-title__subtitle--responsive-sized::text').extract()
        status = response.css('div p.kt-unexpandable-row__value::text').extract()
        detail = response.css('div p.kt-description-row__text--primary::text').extract()
        img = response.css('picture img.kt-image-block__image--fading::text').extract()
        yield {'title': title,
               'description': description,
               'status': status[0],
               'price': status[2],
               'detail': detail,
               'image': img,
               }

# title = response.css('div div.kt-page-title__title--responsive-sized')
# informations = response.css('div div.kt-page-title__subtitle--responsive-sized')
# status = response.css('div p.kt-page-title__subtitle--responsive-sized')
# price = response.css('div p.kt-unexpandable-row__value')
# descriptions = response.css('div div.kt-base-row__start')
# yield {
#     'title': title,
#     'informations': informations,
#     'status': status,
#     'price': price,
#     'descriptions': descriptions
# }

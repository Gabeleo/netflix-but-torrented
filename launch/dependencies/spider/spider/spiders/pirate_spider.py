import scrapy

class PirateSpider(scrapy.Spider):
    name = "pirate"
    start_urls = [
            'https://thepiratebay.org/search/infinity%20war/0/99/0'
        ]

    def parse(self, response):
        resolution = '1080'

        title = response.xpath('//*[@class="detLink"]').attrib['title']

        if title.find(resolution) != -1:
            magnet_link = response.xpath('//*[@title="Download this torrent using magnet"]').attrib['href']
            yield {
                'title': 'https://instant.io/' + '#' + magnet_link
            }
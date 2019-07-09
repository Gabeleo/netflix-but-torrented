import scrapy
from scrapy.http.request import Request
from scrapy.crawler import CrawlerProcess
import json

class PirateSpider(scrapy.Spider):
    name = "pirate"
    start_urls = [
            'https://thepiratebay.org/search/'
        ]
    def start_requests(self):
        with open('urls.json', 'w') as urls:
            for url in urls:
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        resolution = '1080'

        title = response.xpath('//*[@class="detLink"]').attrib['title']

        if title.find(resolution) != -1:
            magnet_link = response.xpath('//*[@title="Download this torrent using magnet"]').attrib['href']
            yield {
                'title': 'https://instant.io/' + '#' + magnet_link
            }
    
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(PirateSpider)
process.start()
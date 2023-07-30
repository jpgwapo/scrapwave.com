import scrapy
from ..items import ScraperItem


class PropertiesSpider(scrapy.Spider):
    name = 'properties'
    start_urls = [
        'https://www.ebay.com/deals'
    ]
    
    def parse(self, response):
        items = ScraperItem()
    
        items['id'] = response.css("div").xpath("@data-listing-id").extract()
        items['name'] = response.css(".ebayui-ellipsis-2::text").extract()
        items['url'] = response.css("div.dne-itemtile-detail a").xpath("@href").extract()
        items['price'] = response.css("span.first::text").extract()
        items['image_url'] = response.css("div.slashui-image-cntr img").xpath("@data-config-src").extract()
            
        yield items

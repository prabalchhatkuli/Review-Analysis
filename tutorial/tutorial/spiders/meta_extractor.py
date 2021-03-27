import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider


class SpidermanSpider(CrawlSpider):
    name = 'meta_crawler'
    allowed_domains = ['redvanplumbingandheating.com']
    start_urls = ['https://www.redvanplumbingandheating.com/']
    decriptionStrings=""
    rules = (
        Rule(LinkExtractor(allow_domains=['redvanplumbingandheating.com']), follow=True, callback="parse_item"),
    )

    def parse_item(self, response):
        address = response.url
        #mail_list = re.findall('\w+@\w+\.{1}\w+', html_text)
        count_address = len(address)
        content_type = response.headers['Content-Type']
        status_code = response.status
        title = response.xpath("//title/text()").extract()
        count_title = len(title[0])
        description = response.xpath("//meta[@name='description']/@content").extract_first()
        if description:
            count_description = len(description)
        else:
            count_description = 0
        keywords = response.xpath("//meta[@name='keywords']/@content").extract_first()
        h1 = response.xpath('//h1//text()').extract_first()
        h2 = response.xpath('//h2//text()').extract_first()
        robot = response.xpath("//meta[@name='robots']/@content").extract_first()
        download_time = response.meta['download_latency']
        if count_description != 0:
            self.decriptionStrings+=description
            yield {'description':self.decriptionStrings}
            '''yield {
                'Address': address,
                'Address count': count_address,
                'Content Type': content_type,
                'Status code': status_code,
                'Title': title,
                'Title count': count_title,
                'Meta description': description,
                'Meta description count': count_description,
                'Meta keywords': keywords,
                'H1': h1,
                'H2': h2,
                'Robot': robot,
                'Download time': download_time
            }'''
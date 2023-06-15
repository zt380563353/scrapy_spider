import scrapy


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ["https://itcast.cn/channel/teacher.shtml"]

    # 爬取结果存到response.body中
    def parse(self, response):
        filename = "teacher.html"
        open(filename, 'wb').write(response.body)

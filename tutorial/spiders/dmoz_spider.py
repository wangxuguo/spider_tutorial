from scrapy.spiders import BaseSpider
class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "https://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, "wb").write(response.body)
from ..items import HousesItem
import scrapy
class HousePrice(scrapy.Spider):
    name = "hscraper"

    # start_urls = [
    #     "https://www.businesslist.pk/category/estate-agents/city:islamabad"
    # ]

    def start_requests(self):
        urls = ['https://www.businesslist.pk/category/estate-agents/1/city:islamabad',
        'https://www.businesslist.pk/category/estate-agents/2/city:islamabad',
        'https://www.businesslist.pk/category/estate-agents/3/city:islamabad',
        'https://www.businesslist.pk/category/estate-agents/4/city:islamabad',
        'https://www.businesslist.pk/category/estate-agents/5/city:islamabad',
        'https://www.businesslist.pk/category/estate-agents/6/city:islamabad',
        'https://www.businesslist.pk/category/estate-agents/7/city:islamabad',
        'https://www.businesslist.pk/category/estate-agents/8/city:islamabad',
        'https://www.businesslist.pk/category/estate-agents/9/city:islamabad',
        'https://www.businesslist.pk/category/estate-agents/10/city:islamabad']


        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)




    def parse(self, response):
        
        urls_ = response.css("h4 a::attr(href)")
        for i in urls_:
            yield response.follow(i.get(), callback=self.get_data)
        # yield {"urls":urls_}
    




        # next_page = response.css("div.pages_container a::attr(href)").get()
        # next_page =response.css('a[rel=next]').attrib['href']
        
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
        



    def get_data(self,response):
        items = HousesItem()
        company_name = response.css("#company_name::text").extract()  
        phone_number = response.css(".phone::text").extract()
        # mobile_number = response.css("div.Mobile phone .text selectorgadget_selected::text").get()
        website = response.css(".weblinks a::text").extract()
        items['company_name'] = company_name
        items['phone_number'] = phone_number
        items['website'] = website

        yield items
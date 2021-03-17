import scrapy

from scrapy.loader import ItemLoader

from ..items import InternationalstandardbankItem
from itemloaders.processors import TakeFirst

base = 'https://international.standardbank.com/services/search/ArticleSearch.jsp?channelID=0de8d1c9e7780710VgnVCM1000008711960a____&articleCTA=Read%20More&keyword=&startIndex={}&endIndex=99999&pageSize=9'

class InternationalstandardbankSpider(scrapy.Spider):
	name = 'internationalstandardbank'
	index = 0
	start_urls = [base.format(index)]

	def parse(self, response):
		post_links = scrapy.Selector(text=response.text).xpath('//div[@class="article-combo-item__link"]/a/@href').getall()
		print(self.index, response, len(post_links))
		yield from response.follow_all(post_links, self.parse_post)

		if post_links:
			self.index += 9
			yield response.follow(base.format(self.index), self.parse)


	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="component text"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//span[@class="page-intro-article__subtitle-date"]/text()').get()

		item = ItemLoader(item=InternationalstandardbankItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()

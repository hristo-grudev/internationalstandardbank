BOT_NAME = 'internationalstandardbank'

SPIDER_MODULES = ['internationalstandardbank.spiders']
NEWSPIDER_MODULE = 'internationalstandardbank.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'internationalstandardbank.pipelines.InternationalstandardbankPipeline': 100,

}

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

BOT_NAME = 'bancadiimola'

SPIDER_MODULES = ['bancadiimola.spiders']
NEWSPIDER_MODULE = 'bancadiimola.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'bancadiimola.pipelines.BancadiimolaPipeline': 100,

}
BOT_NAME = 'crawlers'

SPIDER_MODULES = ['apps.crawlers.spiders']
NEWSPIDER_MODULE = 'apps.crawlers.spiders'

FEED_EXPORT_ENCODING = 'utf-8'

ROBOTSTXT_OBEY = True

DOWNLOAD_FAIL_ON_DATALOSS = True

LOG_ENABLED = False

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'

ITEM_PIPELINES = {
   'apps.crawlers.pipelines.PreprocessPipeline': 100,
   'apps.crawlers.pipelines.ClassificationPipeline':150,
   'apps.crawlers.pipelines.PostgresPipeline': 200
}
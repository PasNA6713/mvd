from multiprocessing import Process

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from twisted.internet.error import ReactorAlreadyRunning
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from .serializers import RunnerSerializer, NewsSerializer
from .spiders.core.services import extract_domain
from .models import NewsModel
from .tasks import insta_parser



process = CrawlerProcess(get_project_settings())


class StartCrawlerView(APIView):
    serializer_class = RunnerSerializer
    
    def post(self, request):
        name = request.data['spider_name']
        try:
            if name == 'explorer':
                urls = [request.data.get('url')]
                if not urls[0]:
                    return Response({'Error': 'Url field is required'}, status=status.HTTP_400_BAD_REQUEST)
                process.crawl(
                    name,
                    start_urls=urls,
                    allowed_domains=[extract_domain(urls[0])]
                )
                
            elif name == 'instagram':
                insta_parser.delay(100, 'навальный')
                return Response(status=status.HTTP_200_OK)

            else:
                process.crawl(name)
                
            p = Process(target=process.start(stop_after_crawl=False))
            p.start()
        except ReactorAlreadyRunning: pass
        return Response(status=status.HTTP_200_OK)


class NewsList(generics.ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
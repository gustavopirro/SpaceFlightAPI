from django.core.management.base import BaseCommand
from api.models import Event
from api.models import Launch
from api.models import Article
import requests
import asyncio
import aiohttp
import math
import platform


class SpaceFlightAPIConsumer():
    articles_count = None
    base_url = None

    def __init__(self) -> None:
        super().__init__()
        self.base_url = 'https://api.spaceflightnewsapi.net/'

    def get_articles_count(self) -> int:
        api_response = requests.get(self.base_url + 'v3/articles/count')
        self.articles_count = api_response.json()
        return self.articles_count

    async def get_all_articles(self) -> list:
        async with aiohttp.ClientSession() as session:
            calls = self.__get_calls__(session)
            responses = await asyncio.gather(*calls)
            fetched_data = []
            count = 0
            for response in responses:
                response = await response.json()
                fetched_data.append(response)
                count += 1

            return fetched_data

    def __get_calls__(self, session):
        if self.articles_count is None:
            self.get_articles_count()

        results_per_page = 1000
        page_index = 0
        articles_pages = math.ceil(self.articles_count / results_per_page)
        api_endpoint = self.base_url + 'v3/articles?_limit={}&_sort=id%3Aasc&_start={}'
        calls = []

        for page in range(0, articles_pages):
            calls.append(
                asyncio.create_task(
                    session.get(
                        api_endpoint.format(results_per_page, page_index), ssl=False
                    )
                )
            )
            page_index += results_per_page
        return calls


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        api_consumer = SpaceFlightAPIConsumer()
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        api_response = asyncio.run(api_consumer.get_all_articles())

        for json_chunk in api_response:
            for item in json_chunk:
                events = item.pop('events')
                launches = item.pop('launches')

                new_article = Article.objects.update_or_create(**item)[0]

                for event in events:
                    event_obj = Event.objects.update_or_create(**event)[0]
                    new_article.events.add(event_obj)

                for launch in launches:
                    launch_obj = Launch.objects.update_or_create(**launch)[0]
                    new_article.launches.add(launch_obj)

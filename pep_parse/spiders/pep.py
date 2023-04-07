from typing import Generator

from scrapy import Spider
from scrapy.http.request import Request
from scrapy.http.response.html import HtmlResponse

from pep_parse.const import FOREPART, NAME, NUMBER
from pep_parse.items import PepParseItem


class PepSpider(Spider):
    """This spider is implemented to parse number, name and status of PEP."""

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response: HtmlResponse) -> Generator[Request, None, None]:
        """Find all links to pep pages."""
        table_rows = response.css('section#numerical-index tbody tr')
        pep_links = table_rows.css('td+td a::attr(href)')
        # Jumping in each link
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response: HtmlResponse) -> PepParseItem:
        """Parsing an information about every pep."""
        information = response.css('section#pep-content')
        page_title = information.css('h1 *::text')
        if len(page_title) == 1:
            number_and_name = page_title.get().split(' – ')
        if len(page_title) > 1:
            number_and_name = information.css('h1 *::text').getall()
            number_and_name = ''.join(number_and_name).split(' – ')
        data = {
            'number': number_and_name[FOREPART].split()[NUMBER],
            'name': number_and_name[NAME],
            'status': information.css('abbr::text').get(),
        }

        return PepParseItem(data)

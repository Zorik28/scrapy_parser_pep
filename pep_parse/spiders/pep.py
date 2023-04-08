from typing import Generator

from scrapy import Spider
from scrapy.http.request import Request
from scrapy.http.response.html import HtmlResponse

from pep_parse.constants import HTTPS_PEPS_PYTHON, ONE_SELECTOR, PEPS_PYTHON
from pep_parse.enums.peps import Pep
from pep_parse.items import PepParseItem


class PepSpider(Spider):
    """This spider is implemented to parse number, name and status of PEP."""

    name = 'pep'
    allowed_domains = [PEPS_PYTHON]
    start_urls = [HTTPS_PEPS_PYTHON]

    def parse(self, response: HtmlResponse) -> Generator[Request, None, None]:
        """Find all links to pep pages."""
        table_rows = response.css('section#numerical-index tbody tr')
        pep_links = table_rows.css('td+td a::attr(href)')
        # Jumping in each link
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response: HtmlResponse) -> PepParseItem:
        """Parsing an information about every pep."""
        main_info = response.css('section#pep-content')
        page_title = main_info.css('h1 *::text')
        if len(page_title) == ONE_SELECTOR:
            number_and_name = page_title.get().split(' – ')
        if len(page_title) > ONE_SELECTOR:
            number_and_name = page_title.getall()
            number_and_name = ''.join(number_and_name).split(' – ')
        data = {
            'number': number_and_name[Pep.title_forepart].split()[Pep.number],
            'name': number_and_name[Pep.name],
            'status': main_info.css('abbr::text').get(),
        }

        return PepParseItem(data)

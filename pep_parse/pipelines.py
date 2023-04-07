import csv
from datetime import datetime

from pep_parse.const import BASE_DIR, DATETIME_FORMAT
from pep_parse.utils import mkdir_and_path


class PepParsePipeline:

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        now = datetime.now()
        filename = now.strftime(DATETIME_FORMAT)
        file_path = mkdir_and_path(BASE_DIR, 'results', filename)
        # Writing data to a file using the context manager in write mode ('w')
        with open(file_path, 'w', encoding='utf-8') as file:
            # dialect='unix' format is to ensure that the data
            # is recorded in the same way on different OS
            writer = csv.writer(file, dialect='unix')
            writer.writerows('fuck')
        return item

    def close_spider(self, spider):
        pass

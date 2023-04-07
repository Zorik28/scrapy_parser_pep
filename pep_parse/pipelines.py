import csv
from datetime import datetime

from pep_parse.const import BASE_DIR, DATETIME_FORMAT
from pep_parse.utils import mkdir_and_path


class PepParsePipeline:
    """Sums the number of documents for each category,
    counts the number of all pep documents."""

    def open_spider(self, spider):
        timestamp = datetime.now().strftime(DATETIME_FORMAT)
        filename = f'status_summary_{timestamp}.csv'
        self.file_path = mkdir_and_path(BASE_DIR, 'results', filename)
        # Set the variables where we will save the data
        self.results = [('Status', 'Quantity', ), ]
        self.status_sum = {}
        self.total = 0

    def process_item(self, item, spider):
        self.total += 1
        if item['status'] not in self.status_sum:
            self.status_sum[item['status']] = 1
        else:
            # Sums the number of documents for each category
            self.status_sum[item['status']] += 1
        return item

    def close_spider(self, spider):
        sorted_status_sum = sorted(self.status_sum.items())
        self.results.extend(sorted_status_sum)
        self.results.append(('Total', self.total))
        # Writing data to a file using the context manager in write mode ('w')
        with open(self.file_path, 'w', encoding='utf-8') as file:
            # dialect='unix' format is to ensure that the data
            # is recorded in the same way on different OS
            writer = csv.writer(file, dialect='unix')
            writer.writerows(self.results)

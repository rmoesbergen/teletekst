#!/usr/bin/env python3
#

import requests
import csv
from sys import argv
from datetime import datetime, date
from os import path


class CsvLogger:
    FIELDS = [
        "datum", "tijd", "av", "vlucht", "locatie", "verwacht"
    ]

    # Filename can contain datetime format specifiers like %M
    def __init__(self, filename):
        self.filename = filename

    def current_filename(self):
        return datetime.now().strftime(self.filename)

    # Logs a Flight object to CSV
    def log(self, flight):
        filename = self.current_filename()
        write_header = not path.exists(filename)
        with open(filename, "a+") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.FIELDS, quoting=csv.QUOTE_NONNUMERIC)
            if write_header:
                writer.writeheader()
            writer.writerow(flight)


class TeletekstScraper:

    AANKOMST_URL = 'https://teletekst-data.nos.nl/webplus?p=768-1'
    VERTREK_URL = 'https://teletekst-data.nos.nl/webplus?p=768-2'

    def __init__(self, filename):
        self.csv_writer = CsvLogger(filename)

    @staticmethod
    def _cleanup(field):
        return field.split('<')[0].strip()

    def parse_flight(self, line):
        parts = line.split('>')

        flight = {
            'datum': date.today(),
            'tijd': self._cleanup(parts[1]),
            'vlucht': self._cleanup(parts[3]),
            'locatie': self._cleanup(parts[5]),
            'verwacht': ""
        }
        if len(parts) >= 8:
            flight['verwacht'] = self._cleanup(parts[7])
            if len(parts) >= 10:
                flight['verwacht'] += " " + self._cleanup(parts[9])

        return flight

    def scrape(self, av):
        url = self.AANKOMST_URL if av == 'Aankomst' else self.VERTREK_URL

        response = requests.get(url)
        if not response.ok:
            raise response.content

        seen_header = False
        for line in response.content.decode('utf8').split("\n"):
            if line.startswith('<span>') and 'Vlucht' in line and not seen_header:
                seen_header = True

            if seen_header and line.startswith('<span class="green'):
                # Found a row of data, parse it
                flight = self.parse_flight(line)
                flight['av'] = av
                self.csv_writer.log(flight)

            if seen_header and line.startswith('<span class="yellow'):
                # Date header found, don't process following records
                break


if __name__ == '__main__':
    filename = argv[1] if len(argv) > 1 else 'teletekst.csv'

    scraper = TeletekstScraper(filename)
    scraper.scrape(av='Aankomst')
    scraper.scrape(av='Vertrek')

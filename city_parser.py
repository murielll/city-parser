# -*- coding: utf-8 -*-
'''
This script parse cities from specified url
and save data in a csv-file named ciies.csv.
'''
from lxml import html
import requests
import csv

COUNTRIES = {
    'AM': {
        'page': 'http://ru.wikipedia.org/wiki/Города_Армении',
        'xpath': ".//*[@id='mw-content-text']/ul/li/b/a/text()"
    },
    'AZ': {
        'page': 'https://ru.wikipedia.org/wiki/Города_Азербайджана',
        'xpath': ".//table[@class='wikitable']//tr/td[1]/a/text() | \
.//table[@class='wikitable']//tr/td[1]/b/a/text()"
    },
    'EE': {
        'page': 'https://ru.wikipedia.org/wiki/Города_Эстонии',
        'xpath': ".//*[@id='mw-content-text']/table[1]//tr/td[2]/a/text()"
    },
    'LT': {
        'page': 'https://ru.wikipedia.org/wiki/Города_Литвы',
        'xpath': ".//*[@id='mw-content-text']/table[2]//tr/td/ul/li/a[1]/\
text()"
    },
    'LV': {
        'page': 'https://ru.wikipedia.org/wiki/Города_Латвии',
        'xpath': "/html/body/div[3]/div[3]/div[4]/div[2]/table//tr/td[1]/a/\
text()"
    },
}


def city_parse(page, xpath, country_code):
    """
    Parse cities from specified page through xpath
    """
    page = requests.get(page)
    html_string = html.fromstring(page.text)
    cities_tmp = html_string.xpath(xpath)

    for city in cities_tmp:
        if city.endswith(")"):
            city = city.split("(")[0].strip()
        yield city.strip().encode("utf-8"), country_code


def parse_all():
    """
    Parse all cities from COUNTRIES dictonary
    """
    for country, opt in COUNTRIES.items():
        cities = city_parse(page=opt['page'], xpath=opt['xpath'],
                            country_code=country)
        for city in cities:
            yield city


def write_in_csv(out_file, header, lines):
    """
    Write city and iso country code in csv file
    """
    with open(out_file, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header)
        for line in lines:
            writer.writerow(line)


def save_all_data(out_file):
        header = ['title', 'country']
        data = parse_all()
        write_in_csv(out_file, header, data)


if __name__ == '__main__':
    save_all_data(out_file='cities.csv')

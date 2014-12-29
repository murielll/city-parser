# -*- coding: utf-8 -*-
from lxml import html
import requests
import codecs


def city_parse(country_code='', page='', xpath=''):
    if not country_code and not country_code and not xpath:
        return "Error parse for %s! Specify all args!" % country_code

    page = requests.get(page)
    html_string = html.fromstring(page.text)
    cities = list()
    cities_tmp = html_string.xpath(xpath)
    for city in cities_tmp:
        if city.endswith(")"):
            city = city.split("(")[0].strip()
        cities.append(city.strip())

    with codecs.open(country_code + '.txt', 'w', encoding='utf-8') as output:
        for city in cities:
            city = u"%s\n" % city
            output.write(city)

    print"Parse %s OK!" % country_code

Azerbajan = dict(
    country_code='AZ',
    page='https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0_\
    %D0%90%D0%B7%D0%B5%D1%80%D0%B1%D0%B0%D0%B9%D0%B4%D0%B6%D0%B0%D0%BD%D0%B0',
    xpath=".//table[@class='wikitable']//tr/td[1]/a/text() | \
    .//table[@class='wikitable']//tr/td[1]/b/a/text()"
)

Armenia = dict(
    country_code='AM',
    page='http://obzorurokov.ru/armeniya/\
    goroda-armenii-spisok-po-alfavitu.html',
    xpath=".//*[@id='overall']/div[2]/div[2]/div[1]/div/div[2]/div/\
    p[position()>1]/text()"
)

Estonia = dict(
    country_code='EE',
    page='https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0\
    _%D0%AD%D1%81%D1%82%D0%BE%D0%BD%D0%B8%D0%B8',
    xpath=".//*[@id='mw-content-text']/table[1]//tr/td[2]/a/text()"
)

Litwa = dict(
    country_code='LT',
    page='https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0\
    _%D0%9B%D0%B8%D1%82%D0%B2%D1%8B',
    xpath=".//*[@id='mw-content-text']/table[2]//tr/td/ul/li/a[1]/text()"
)

Latwia = dict(
    country_code='LV',
    page='https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0\
    _%D0%9B%D0%B0%D1%82%D0%B2%D0%B8%D0%B8',
    xpath="/html/body/div[3]/div[3]/div[4]/div[2]/table//tr/td[1]/a/text()"
)

COUNTRIES = [Armenia, Azerbajan, Estonia, Litwa, Latwia]
#COUNTRIES = [Latwia, ]
for country in COUNTRIES:
    city_parse(country_code=country['country_code'],
               page=country['page'], xpath=country['xpath'])

print "\nFinish!"

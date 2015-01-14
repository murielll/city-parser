# -*- coding: utf-8 -*-
'''
Script load in DB cities which there is not yet in DB.
Before run:
- copy this script and csv file cities.csv in directory with manage.py
- export enviroment variable (export DJANGO_SETTINGS_MODULE=settings)
'''
import codecs
from goroda.models import City


def load_data(in_file='cities.csv'):
    with codecs.open(in_file, encoding='utf-8') as input_file:
        for line in input_file.readlines()[1:]:
            title, country = line.split(",")
            country = country.strip()
            city_create = City.objects.get_or_create(title=title,
                                                     country=country)
            if city_create[1]:
                msg = "# City << %s >> inserted in DB! #\n" % title
                brd = '#' * (len(msg) - 1) + '\n'
                print brd + msg + brd
            else:
                msg = "!! City << %s >> is alredy in DB! !!\n" % title
                brd = '!' * (len(msg) - 1) + '\n'
                print brd + msg + brd
    print ("Done!")


if __name__ == '__main__':
    load_data()

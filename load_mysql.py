# -*- coding: utf-8 -*-
'''
Script load in DB cities which there is not yet in DB.
'''
from __future__ import unicode_literals
import codecs
import MySQLdb


db = MySQLdb.connect(host="localhost",
                     user="cubertin",
                     passwd="cubertin",
                     db="cubertin",
                     charset='utf8',
                     use_unicode=True)

cursor = db.cursor()

with codecs.open('united.csv', encoding='utf-8') as input_file:
    for line in input_file.readlines()[1:]:
        title, country = line.split(",")
        country = country.strip()
        sql = """SELECT country,title FROM goroda_city WHERE country='%s' and\
         title='%s'""" % (country, title)
        cursor.execute(sql)
        if cursor.fetchall():
            print "<---\nCity << %s >> is alredy in DB!\n--->\n" % title
            continue
        else:
            sql = """INSERT INTO goroda_city (country, title) VALUES \
            ('%s', '%s')""" % (country, title)
            cursor.execute(sql)
            db.commit()
            print "######\nCity << %s >> inserted in DB!\n######\n" % title


db.close()
print ("Done!")

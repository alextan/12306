import urllib2
import json
import sys
import config

target_train_no = "D2101"
query = config.LeftTicket("2014-06-22","YDQ","GZQ")
print query.url
response = urllib2.urlopen(query.url)
html = json.loads(response.read())
for train in eval(query.json_format):
    if train[config.train_no] == target_train_no:
       print "seat_ydz:", train[config.seats['ydz']] 
       print "seat_edz:", train[config.seats['edz']] 
       print "seat_swz:", train[config.seats['swz']] 

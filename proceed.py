import urllib2
import json
import sys
from config import *

no = "G1013"
query = LeftTicket("2014-06-20","YDQ","GZQ")
print query.url
response = urllib2.urlopen(query.url)
html = json.loads(response.read())
train = [train for train in eval(query.json_format) if no == train[train_no]][0]
seat = {(k,train[v]) for (k,v) in seats.items() if train[v] != '--'}
for (k,v) in seat:
    print k, v
#for (k,v) in seats.items():
#    if train[v] != '--':
#        print k, ":", train[v]
#print "seat_ydz:", train[0][seats['ydz']]
#print "seat_edz:", train[0][seats['edz']]
#print "seat_swz:", train[0][seats['swz']]

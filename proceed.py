import urllib2
import json
import sys
from config import *

no = "G1013"
query = LeftTicketConfig("2014-06-20","YDQ","GZQ")
print query.url
response = urllib2.urlopen(query.url)
html = json.loads(response.read())
train = [train for train in eval(query.json_format) if no == train[train_no]][0]
print train

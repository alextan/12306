import re
import requests
import sys
from config import *

no = "G1013"
query = LeftTicketConfig("2014-06-20","YDQ","GZQ")
print query.url
response = requests.get(query.url, verify=False)
html = response.json()
train = [train for train in eval(query.json_format) if no == train[train_no]][0]
print dict((seats[k], train[v]) for (k,v) in seats.items() if re.compile(r'\d+').match(train[v]))

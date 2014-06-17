import re
import urllib2
import json
import config

def checkLeftTicket (train_no, date, from_station, to_station):
    proceed = config.LeftTicketConfig(date,from_station,to_station)
    print proceed.url
    response = urllib2.urlopen(proceed.url)
    html = json.loads(response.read())
    train = [train for train in eval(proceed.json_format) if train_no == train[config.train_no]][0]
    return json.dumps(dict((k,train[v]) for (k,v) in config.seats.items() if re.compile(r'\d+').match(train[v])))

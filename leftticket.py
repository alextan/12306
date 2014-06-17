import re
import urllib2
import json
import sys
import config

class LeftTicket:
    def __init__ (self, train_no, date, from_station, to_station):
        proceed = config.LeftTicketConfig(date,from_station,to_station)
        print proceed.url
        response = urllib2.urlopen(proceed.url)
        html = json.loads(response.read())
        train = [train for train in eval(proceed.json_format) if train_no == train[config.train_no]][0]
        self.avail_seat = json.dumps(dict((k,train[v]) for (k,v) in config.seats.items() if re.compile(r'\d+').match(train[v])))

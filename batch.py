import json
from leftticket import *
import codecs

with codecs.open('queue.json', 'r', encoding='utf-8') as jsonfile:
    queue = json.load(jsonfile)
for (k,v) in queue.items():
    date = queue[k]['date']
    to_station = queue[k]['to_station']
    from_station = queue[k]['from_station']
    train_no = queue[k]['train_no']
    avail_seats = checkLeftTicket(train_no, date, from_station, to_station)
    if len(avail_seats) > 0:
        print queue[k]['users'], avail_seats
        del queue[k]


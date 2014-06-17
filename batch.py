from config import *
from leftticket import *

for job in queue:
    date = job['date']
    to_station = job['to_station']
    from_station = job['from_station']
    train_no = job['train_no']
    avail_seats = checkLeftTicket(train_no, date, from_station, to_station)
    if len(avail_seats) > 0:
        informUser(avail_seats)

def informUser(avail_seats)


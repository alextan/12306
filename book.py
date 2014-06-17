import leftticket
import config

class BookLeftTicketReminder:
    def __init__ (self, train_no, date, from_station, to_station, seats, userid):
        config.leftticket_queue.append({'train_no':train_no,'date':date,'from_station':from_station, 'to_station':to_station, 'seats':seats, 'userid':userid})

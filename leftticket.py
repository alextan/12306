import web
import config
import json
import urllib2

class leftticket_proceed:
    
    def __init__ (self, train_no, departure, destination):
        self.train_no = train_no
        self.departure = departure
        self.destination = destination

    def query ():
        leftticket = config.LeftTicket(train_no, departure, destination)
        response = urllib2.urlopen(leftticket.url)
        html = json.loads(response.read())
        for train in eval(leftticket.json_format):
            if train[config.train_no] == destination:
                switch 

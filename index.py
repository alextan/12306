import config
import web
import leftticket
import json
import hashlib

urls = (
    '/', 'index',
    '/leftticket','queryleftticket',
    '/bookrequest','bookrequest',
    '/12306','wechat'
)

class wechat:
    def GET(self):
        url_data = web.input()
        signature = url_data.signature
        timestamp = url_data.timestamp
        nonce = url_data.nonce
        token = 'magiccode'
        echostr = url_data.echostr
        print signature, timestamp, nonce, token, 
        list = [token,timestamp,nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        if hashcode == signature:
            return echostr


class index:
    def GET(self):
        hello = web.template.frender('templates/hello.html')
        return hello('world')

class queryleftticket:
    def GET(self):
        web.header('Content-Type','application/json; charset=utf-8', unique=True)
        url_data = web.input()
        return json.dumps(leftticket.checkLeftTicket(url_data.train_no, url_data.date, url_data.from_station, url_data.to_station))

class bookrequest:
    def GET(self):
        web.header('Content-Type','application/json; charset=utf-8', unique=True)
        url_data = web.input(seats=[])
        date            = url_data.date
        train_no        = url_data.train_no
        from_station    = url_data.from_station
        to_station      = url_data.to_station
        userid          = url_data.userid
        seats           = url_data.seats
        key = date + train_no + from_station + to_station
        print key
        if config.queue.has_key(key):
            config.queue[key]['users'][userid] = seats
        else:
            config.queue[key] = {'date':date,'train_no':train_no,'from_station':from_station,'to_station':to_station, 'users': { userid:seats }}
        return json.dumps(config.queue)

if __name__ == "__main__":
    app = web.application (urls, globals())
    app.run()

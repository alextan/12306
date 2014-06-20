import config
import web
import json

urls = (
    '/', 'testbatch'
    )
class testbatch:
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

import web
import leftticket

urls = (
    '/', 'index',
    '/leftticket','queryleftticket'
)

class index:
    def GET(self):
        hello = web.template.frender('templates/hello.html')
        return hello('world')

class queryleftticket:
    def GET(self):
        url_data = web.input()
        request_leftticket = leftticket.LeftTicket(url_data.train_no, url_data.date, url_data.from_station, url_data.to_station)
        return request_leftticket.avail_seat

if __name__ == "__main__":
    app = web.application (urls, globals())
    app.run()

import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        hello = web.template.frender('templates/hello.html')
        return hello('world')

if __name__ == "__main__":
    app = web.application (urls, globals())
    app.run()

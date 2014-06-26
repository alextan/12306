import web
import hashlib
import json

urls = (
        '/','index',
        '/12306','wetoken'
        )

class index:
    def GET(self):
        return "Hello, Welcome"

class wetoken:
    def GET(self):
#        return "hellow token"
        url_data = web.input()
        signature = url_data.signature
        timestamp = url_data.timestamp
        nonce = url_data.nonce
        tokencode = 'magiccode'
        echostr = url_data.echostr
        print signature, timestamp, nonce, tokencode,
        list = [tokencode,timestamp,nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        if hashcode == signature:
            return echostr

if __name__ == "__main__":
    app = web.application (urls, globals())
    app.run()

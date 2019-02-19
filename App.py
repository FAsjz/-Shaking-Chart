from tornado import web,ioloop,httpserver
import os

class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
	    self.render("wopop.html")

application = web.Application([
            (r"/", MainPageHandler),],
            static_path = os.path.join(os.path.dirname(__file__), "static"),
        )
def main():
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
# Tornado is more robust - consider using over Flask if do not need to worry about templates?

import logging
import socket
import sys
import os

import tornado.ioloop
import tornado.web
import tornado.options


class BaseHandler(tornado.web.RequestHandler):
    # This is a handler that will get associated with an endpoint

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')


class UploadHandler(BaseHandler):
    def post(self, name=None):  # I *think* name is the sub endpoint?
        # NOTE - if you pass self.write a dictionary, it will automatically write out
        # JSON and set the content type to JSON
        print("recieved a file")
        pic = self.request.files['file'][0]
        fname = pic['filename']
        output_file = open("img/" + fname, 'wb')
        output_file.write(pic['body'])
        self.write({"msg": "Hello, World!"})
        # Other methods: self.redirect, self.get_argument, self.request.body,
        #img = Image.open(StringIO.StringIO(file_body))
        #img.save("/img", img.format)


class MainHandler(BaseHandler):
    def get(self, name=None):  # I *think* name is the sub endpoint?
        # NOTE - if you pass self.write a dictionary, it will automatically write out
        # JSON and set the content type to JSON
        self.write({"msg": "Hello, World!"})
        # Other methods: self.redirect, self.get_argument, self.request.body,


class MainApplication(tornado.web.Application):
    def __init__(self, **settings):
        tornado.web.Application.__init__(self, **settings)
        # Add in various member variables here that you want the handlers to be aware of
        # e.g. a database client

        # Add the handlers here - use regular expressions or hardcoded paths to link the endpoints
        # with handlers?
        self.port = 8888
        self.address = "127.0.0.1"
        self.ioloop = tornado.ioloop.IOLoop.instance()
        self.logger = logging.getLogger()

        # Tie the handlers to the routes here
        self.add_handlers('.*', [
            (r'.*/(.*)', MainHandler),
        ])

    def run(self):
        try:
            self.listen(self.port, self.address)
        except socket.error as e:
            self.logger.fatal('Unable to listen on {}:{} = {}'.format(
                self.address, self.port, e))
            sys.exit(1)

        self.ioloop.start()


if __name__ == "__main__":
    tornado.options.define('debug', default=False,
                           help='Enable debugging mode.')

    tornado.options.parse_command_line()
    options = tornado.options.options.as_dict()
    app = MainApplication(**options)
    app.run()

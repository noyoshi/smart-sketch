# Tornado is more robust - consider using over Flask if do not need to worry about templates?

import logging
import socket
import sys
import os
import uuid
import subprocess
# import magic

import tornado.ioloop
import tornado.web
import tornado.options

IMG_FOLDER = os.path.join(os.path.dirname(__file__), 'img')


def determine_mimetype(path):
    try:
        result = subprocess.check_output(['file', '--mime-type', path])
    except subprocess.CalledProcessError:
        result = '{}: text/plain'.format(path)

    return result.decode('utf8').split(':', 1)[-1].strip()


class BaseHandler(tornado.web.RequestHandler):
    # This is a handler that will get associated with an endpoint

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers",
                        "x-requested-with, Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()


class UploadHandler(BaseHandler):
    def post(self, name=None):  # This only recieves one file at a time...
        # NOTE - if you pass self.write a dictionary, it will automatically write out
        # JSON and set the content type to JSON
        pic = self.request.body
        fname = uuid.uuid4().hex
        relative_path = 'img/' + fname
        output_file_path = IMG_FOLDER + '/' + fname

        # Writes a temp file so we can get the mime type
        temp = IMG_FOLDER + '/' + 'temp'
        with open(temp, 'wb') as out_f:
            out_f.write(pic)

        # Gets the mimetype from the temp file
        mime_type = determine_mimetype(temp).split('/')[1]

        # Append the mimetype ending to the end of this file, and write it out
        with open(output_file_path + '.' + mime_type, 'wb') as out_f:
            out_f.write(pic)

        self.write({"result": "success",
                    "location": relative_path})


class MainHandler(BaseHandler):
    def get(self, path, name=None):  # I *think* name is the sub endpoint?
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
            (r'/', MainHandler),
            (r'/upload', UploadHandler),
            (r'/img/(.*)', tornado.web.StaticFileHandler, {'path': IMG_FOLDER})
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

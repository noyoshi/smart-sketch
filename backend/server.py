# Tornado is more robust - consider using over Flask if do not need to worry about templates?

import logging
import socket
import sys
import os
import subprocess

import tornado.ioloop
import tornado.web
import tornado.options

IMG_FOLDER = os.path.join(os.path.dirname(__file__), 'dataset/val_img')
INST_FOLDER = os.path.join(os.path.dirname(__file__), 'dataset/val_inst')
LABEL_FOLDER = os.path.join(os.path.dirname(__file__), 'dataset/val_label')

# This is where the image will go 
EXPORT_LOCATION = os.path.join(os.path.dirname(__file__), 'results/coco_pretrained/test_latest/images/synthesized_image')


def run_model(filepath):
    '''Runs the pretrained COCO model'''
    # TODO check to see if this goes any faster with GPUS enabled...
    command_string = "python3 test.py --name coco_pretrained --dataset_mode coco --dataroot dataset/ --gpu_ids -1 --no_pairing_check"
    command = command_string.split(' ')
    result = subprocess.check_output(command)


class BaseHandler(tornado.web.RequestHandler):
    # This is a handler that will get associated with an endpoint

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()


class UploadHandler(BaseHandler):
    def post(self, name=None):  # I *think* name is the sub endpoint?
        # NOTE - if you pass self.write a dictionary, it will automatically write out
        # JSON and set the content type to JSON
        # TODO Fix this with how we will be getting the file from the front end...

        # TODO change the way that we save the model?
        print("recieved a file")
        pic = self.request.files['file'][0]
        fname = pic['filename']
        relative_path = 'img/' + fname
        output_file_path = IMG_FOLDER + '/' + fname

        with open(output_file_path, 'wb') as out_f:
            out_f.write(pic['body'])

        run_model('')

        # TODO change the relative path here to be the path to the image generated - IE 
        # the thingy you generated earlier...
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

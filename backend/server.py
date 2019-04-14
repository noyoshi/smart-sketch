# Tornado is more robust - consider using over Flask if do not need to worry about templates?

import logging
import socket
import sys
import os
import subprocess
import base64
import uuid

import tornado.ioloop
import tornado.web
import tornado.options
from color_grey_conversion import color_to_grey

IMG_FOLDER = os.path.join(os.path.dirname(__file__), 'dataset/val_img')
INST_FOLDER = os.path.join(os.path.dirname(__file__), 'dataset/val_inst')
LABEL_FOLDER = os.path.join(os.path.dirname(__file__), 'dataset/val_label')

# This is where the image will go
EXPORT_LOCATION = os.path.join(os.path.dirname(
    __file__), 'results/coco_pretrained/test_latest/images/synthesized_image')
STATIC_IMG_FOLDER = os.path.join(os.path.dirname(__file__), 'img')


def check_for_dataset_folder():
    if not os.path.isdir("dataset/"):
        os.mkdir("dataset/")
    if not os.path.isdir("dataset/val_img"):
        os.mkdir("dataset/val_img")
    if not os.path.isdir("dataset/val_inst"):
        os.mkdir("dataset/val_inst")
    if not os.path.isdir("dataset/val_label"):
        os.mkdir("dataset/val_label")


def run_model(filename):
    '''Runs the pretrained COCO model'''
    # TODO check to see if this goes any faster with GPUS enabled...
    # TODO make is it so that concurrent users won't mess with eachother :P aka have hashed or something dataset routes...
    # that will also take a lot of cleaning up...
    command_string = "python3 test.py --name coco_pretrained --dataset_mode coco --dataroot dataset/ --gpu_ids -1 --no_pairing_check"
    command = command_string.split(' ')
    result = subprocess.check_output(command)
    return EXPORT_LOCATION + '/' + filename


def copy_file(old="avon.png", new="avon.png"):
    command_string = "cp " + old + " " + new
    subprocess.check_output(command_string.split(' '))


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


def make_processable(greyscale_fname, output_color_file):
        # Inst folder
    ouptut_greyscale_file = INST_FOLDER + '/' + greyscale_fname

    # Converts the file to greyscale and saves it to the inst folder?
    color_to_grey.convert_rgb_image_to_greyscale(
        output_color_file, ouptut_greyscale_file)

    ouptut_greyscale_file_labels = LABEL_FOLDER + '/' + greyscale_fname

    copy_file(ouptut_greyscale_file, ouptut_greyscale_file_labels)

    ouptut_greyscale_file_img = IMG_FOLDER + '/' + greyscale_fname
    copy_file(ouptut_greyscale_file, ouptut_greyscale_file_img)


def export_image(greyscale_fname):
    current_image_location = EXPORT_LOCATION + "/" + greyscale_fname
    export_image_location = STATIC_IMG_FOLDER + \
        "/" + uuid.uuid4().hex + greyscale_fname
    copy_file(current_image_location, export_image_location)
    return export_image_location


class UploadHandler(BaseHandler):
    def post(self, name=None):
        # TODO Fix this with how we will be getting the file from the front end...

        # TODO change the way that we save the model?
        self.application.logger.info("Recieved a file")
        pic = str(self.request.body)
        # print(pic.split(','))
        base64_string = pic.split(',')[1]
        img_data = base64.b64decode(base64_string)
        color_fname = "color.png"
        # relative_path = 'img/' + color_fname
        output_color_file = STATIC_IMG_FOLDER + '/' + color_fname

        # Writes the color image
        with open(output_color_file, 'wb+') as out_f:
            out_f.write(img_data)

        greyscale_fname = "greyscale.png"

        make_processable(greyscale_fname, output_color_file)

        # We shouldnt need to pass it a string anymore
        _ = run_model(greyscale_fname)
        # Where is the final image??

        export_image_location = export_image(greyscale_fname)

        # TODO change the relative path here to be the path to the image generated - IE
        # the thingy you generated earlier...
        self.write({"result": "success",
                    "location": export_image_location})


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
            (r'/img/(.*)', tornado.web.StaticFileHandler,
             {'path': STATIC_IMG_FOLDER})
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
    check_for_dataset_folder()
    tornado.options.define('debug', default=False,
                           help='Enable debugging mode.')

    tornado.options.parse_command_line()
    options = tornado.options.options.as_dict()
    app = MainApplication(**options)
    app.run()

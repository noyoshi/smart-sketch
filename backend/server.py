# Tornado is more robust - consider using over Flask if do not need to worry about templates?

import base64
import logging
import os
import socket
import subprocess
import sys
import uuid
from test import run

import tornado.ioloop
import tornado.options
import tornado.web
import signal

from color_grey_conversion import color_to_grey

IMG_FOLDER = os.path.join(os.path.dirname(__file__), "dataset/val_img")
INST_FOLDER = os.path.join(os.path.dirname(__file__), "dataset/val_inst")
LABEL_FOLDER = os.path.join(os.path.dirname(__file__), "dataset/val_label")

verbose = ((sys.argv[1] if 1 < len(sys.argv) else "")=="verbose")

STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'static')

# This is where the temp image will go
EXPORT_LOCATION = "/tmp"

STATIC_IMG_FOLDER = os.path.join(
    os.path.dirname(__file__),
    "img"
)


def check_for_dataset_folder():
    if not os.path.isdir("dataset/"):
        os.mkdir("dataset/")
    if not os.path.isdir("dataset/val_img"):
        os.mkdir("dataset/val_img")
    if not os.path.isdir("dataset/val_inst"):
        os.mkdir("dataset/val_inst")
    if not os.path.isdir("dataset/val_label"):
        os.mkdir("dataset/val_label")


def parse_static_filepath(filepath):
    split_filepath = filepath.split('/')
    while len(split_filepath) > 2:
        split_filepath.pop(0)

    return '/'.join(split_filepath)


def run_model(filename):
    """Runs the pretrained COCO model"""
    # TODO check to see if this goes any faster with GPUS enabled...
    # TODO make is it so that concurrent users won't mess with eachother :P aka have hashed or something dataset routes...
    # that will also take a lot of cleaning up...
    # TODO figure out how to not do this from the command line...
    return run(verbose=verbose)


def copy_file(old="avon.png", new="avon.png"):
    command_string = "cp " + old + " " + new
    subprocess.check_output(command_string.split(" "))


def make_processable(greyscale_fname, output_color_file):
    # Inst folder
    ouptut_greyscale_file = INST_FOLDER + "/" + greyscale_fname

    # Converts the file to greyscale and saves it to the inst folder?
    if verbose:
        print(output_color_file, ouptut_greyscale_file)
    color_to_grey.convert_rgb_image_to_greyscale(
        output_color_file,
        ouptut_greyscale_file
    )

    ouptut_greyscale_file_labels = LABEL_FOLDER + "/" + greyscale_fname

    copy_file(ouptut_greyscale_file, ouptut_greyscale_file_labels)

    ouptut_greyscale_file_img = IMG_FOLDER + "/" + greyscale_fname
    copy_file(ouptut_greyscale_file, ouptut_greyscale_file_img)

# def export_image(greyscale_fname):
#     current_image_location = EXPORT_LOCATION + "/" + greyscale_fname
#     export_image_location = STATIC_IMG_FOLDER + \
#         "/" + uuid.uuid4().hex + greyscale_fname
#     copy_file(current_image_location, export_image_location)
#     return export_image_location


class UploadHandler(tornado.web.RequestHandler):
    def post(self, name=None):
        # TODO Fix this with how we will be getting the file from the front end...
        # TODO change the way that we save the model?
        self.application.logger.info("Recieved a file")
        pic = str(self.request.body)
        # print(pic.split(','))
        base64_string = pic.split(",")[1]
        img_data = base64.b64decode(base64_string)
        color_fname = "color.png"
        # relative_path = "img/" + color_fname
        output_color_file = STATIC_IMG_FOLDER + "/" + color_fname

        # Writes the color image
        with open(output_color_file, "wb+") as out_f:
            out_f.write(img_data)

        greyscale_fname = "greyscale.png"

        make_processable(greyscale_fname, output_color_file)

        # We shouldnt need to pass it a string anymore
        export_image_location = run_model(greyscale_fname)
        if verbose:
            print(export_image_location)
        static_image_location = parse_static_filepath(export_image_location)
        if verbose:
            print(static_image_location)

        self.write({
            "result": "success",
            "location": static_image_location
        })


class MainHandler(tornado.web.RequestHandler):
    def get(self, name=None):  # I *think* name is the sub endpoint?
        # NOTE - if you pass self.write a dictionary, it will automatically write out
        # JSON and set the content type to JSON
        self.render("index.html")
        # Other methods: self.redirect, self.get_argument, self.request.body,


class MainApplication(tornado.web.Application):
    is_closing = False

    def signal_handler(self, signum, frame):
        logging.info('exiting...')
        self.is_closing = True

    def try_exit(self):
        if self.is_closing:
            tornado.ioloop.IOLoop.instance().stop()
            logging.info('exit success')

    def __init__(self, **settings):
        tornado.web.Application.__init__(self, **settings)
        # Add in various member variables here that you want the handlers to be aware of
        # e.g. a database client

        # Add the handlers here - use regular expressions or hardcoded paths to link the endpoints
        # with handlers?
        self.port = settings.get('port', 80)
        self.address = settings.get('address', "0.0.0.0")
        self.ioloop = tornado.ioloop.IOLoop.instance()
        self.logger = logging.getLogger()

        # Tie the handlers to the routes here
        self.add_handlers(".*", [
            (r"/", MainHandler),
            (r"/upload", UploadHandler),
            (r"/img/(.*)", tornado.web.StaticFileHandler,
             {"path": STATIC_IMG_FOLDER}),
            (r".*/static/(.*)", tornado.web.StaticFileHandler,
             {"path": STATIC_FOLDER})
        ])

    def run(self):
        try:
            signal.signal(signal.SIGINT, self.signal_handler)
            self.listen(self.port, self.address)
            tornado.ioloop.PeriodicCallback(self.try_exit, 100).start()

        except socket.error as e:
            self.logger.fatal("Unable to listen on {}:{} = {}".format(
                self.address, self.port, e))
            sys.exit(1)
        self.ioloop.start()


if __name__ == "__main__":

    check_for_dataset_folder()
    tornado.options.define(
        "debug",
        default=False,
        help="Enable debugging mode."
    )
    tornado.options.define('port', default=80, help='Port to listen on.')
    host = "0.0.0.0"
    if sys.platform == "win32":
        host = "127.0.0.1"
    tornado.options.define('address', default=host, help='Url')

    tornado.options.define('template_path', default=os.path.join(
        os.path.dirname(__file__), "templates"), help='Path to templates')
    tornado.options.parse_command_line()
    options = tornado.options.options.as_dict()
    if verbose:
        print(options)
    app = MainApplication(**options)
    app.run()

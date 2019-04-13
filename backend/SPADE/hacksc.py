"""
Copyright (C) 2019 NVIDIA Corporation.  All rights reserved.
Licensed under the CC BY-NC-SA 4.0 license (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).
"""

import os
from collections import OrderedDict

import data
from options.test_options import TestOptions
from models.pix2pix_model import Pix2PixModel
from util.visualizer import Visualizer
from util import html

# opt = argparse.Namespace

#python test.py --name coco_pretrained --dataset_mode coco --dataroot datasets/coco_stuff/ --gpu_ids -1

"""
    def parse(self, save=False):

        opt = self.gather_options()
        opt.isTrain = self.isTrain   # train or test

        self.print_options(opt)
        if opt.isTrain:
            self.save_options(opt)

        # Set semantic_nc based on the option.
        # This will be convenient in many places
        opt.semantic_nc = opt.label_nc + \
            (1 if opt.contain_dontcare_label else 0) + \
            (0 if opt.no_instance else 1)

        # set gpu ids
        str_ids = opt.gpu_ids.split(',')
        opt.gpu_ids = []
        for str_id in str_ids:
            id = int(str_id)
            if id >= 0:
                opt.gpu_ids.append(id)
        if len(opt.gpu_ids) > 0:
            torch.cuda.set_device(opt.gpu_ids[0])

        assert len(opt.gpu_ids) == 0 or opt.batchSize % len(opt.gpu_ids) == 0, \
            "Batch size %d is wrong. It must be a multiple of # GPUs %d." \
            % (opt.batchSize, len(opt.gpu_ids))

        self.opt = opt
        return self.opt
"""

"""
def gather_options(self):
    # initialize parser with basic options
    if not self.initialized:
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser = self.initialize(parser)

    # get the basic options
    # opt = argparse.Namespace
    opt, unknown = parser.parse_known_args()

    # modify model-related parser options
    model_name = opt.model
    model_option_setter = models.get_option_setter(model_name)
    parser = model_option_setter(parser, self.isTrain)

    # modify dataset-related parser options
    dataset_mode = opt.dataset_mode
    dataset_option_setter = data.get_option_setter(dataset_mode)
    parser = dataset_option_setter(parser, self.isTrain)

    opt, unknown = parser.parse_known_args()

    # if there is opt_file, load it.
    # The previous default options will be overwritten
    if opt.load_from_opt_file:
        parser = self.update_options_from_file(parser, opt)

    opt = parser.parse_args()
    self.parser = parser
    return opt
"""

"""
def initialize(self, parser):
    BaseOptions.initialize(self, parser)
    parser.add_argument('--results_dir', type=str, default='./results/', help='saves results here.')
    parser.add_argument('--which_epoch', type=str, default='latest', help='which epoch to load? set to latest to use latest cached model')
    parser.add_argument('--how_many', type=int, default=float("inf"), help='how many test images to run')

    parser.set_defaults(preprocess_mode='scale_width_and_crop', crop_size=256, load_size=256, display_winsize=256)
    parser.set_defaults(serial_batches=True)
    parser.set_defaults(no_flip=True)
    parser.set_defaults(phase='test')
    self.isTrain = False
    return parser
"""

opt = TestOptions().parse()


"""
def create_dataloader(opt):
    dataset = find_dataset_using_name(opt.dataset_mode)
    instance = dataset()
    instance.initialize(opt)
    print("dataset [%s] of size %d was created" %
          (type(instance).__name__, len(instance)))
    dataloader = torch.utils.data.DataLoader(
        instance,
        batch_size=opt.batchSize,
        shuffle=not opt.serial_batches,
        num_workers=int(opt.nThreads),
        drop_last=opt.isTrain
    )
    return dataloader
"""
dataloader = data.create_dataloader(opt)

model = Pix2PixModel(opt)
model.eval()

visualizer = Visualizer(opt)

# create a webpage that summarizes the all results
web_dir = os.path.join(opt.results_dir, opt.name,
                       '%s_%s' % (opt.phase, opt.which_epoch))
#print("web_dir: ",web_dir)
webpage = html.HTML(web_dir,
                    'Experiment = %s, Phase = %s, Epoch = %s' %
                    (opt.name, opt.phase, opt.which_epoch))
# test
for i, data_i in enumerate(dataloader):
    if i * opt.batchSize >= opt.how_many:
        break

    generated = model(data_i, mode='inference')

    img_path = data_i['path']
    for b in range(generated.shape[0]):
        #visuals = OrderedDict([('input_label', data_i['label'][b]),('synthesized_image', generated[b])])
        visuals_1 = OrderedDict([('synthesized_image', generated[b])])
        #visualizer.save_images(webpage, visuals, img_path[b:b + 1])
        visualizer.save_images_no_webpage(webpage.get_image_dir(),generated[b], img_path[b:b + 1])

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

# python test.py --name coco_pretrained --dataset_mode coco --dataroot datasets/coco_stuff/ --gpu_ids -1

# --gpu_ids


opt = TestOptions().parse()
dataloader = data.create_dataloader(opt)
model = Pix2PixModel(opt)
model.eval()


# keep
visualizer = Visualizer(opt)
# create a webpage that summarizes the all results
web_dir = os.path.join(opt.results_dir, opt.name,
                       '%s_%s' % (opt.phase, opt.which_epoch))
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
        print('process image... %s' % img_path[b])
        visualizer.save_images_no_webpage(
            webpage.get_image_dir(), generated[b], img_path[b:b + 1])

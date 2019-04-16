"""
Copyright (C) 2019 NVIDIA Corporation.  All rights reserved.
Licensed under the CC BY-NC-SA 4.0 license (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).
"""

import importlib
import os
from collections import OrderedDict

import torch

import data
from data.base_dataset import BaseDataset
from models.pix2pix_model import Pix2PixModel
from options.test_options import TestOptions
from util import html
from util.visualizer import Visualizer


def run():
    opt = TestOptions().parse()

    dataset_name = "coco"
    dataset_filename = "data." + dataset_name + "_dataset"

    datasetlib = importlib.import_module(dataset_filename)

    dataset = None
    target_dataset_name = dataset_name.replace('_', '') + 'dataset'
    for name, cls in datasetlib.__dict__.items():
        if name.lower() == target_dataset_name.lower() \
            and issubclass(cls, BaseDataset):
            dataset = cls

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

    model = Pix2PixModel(opt)
    model.eval()

    visualizer = Visualizer(opt)
    print(dataloader)

    for i, data_i in enumerate(dataloader):
        if i * opt.batchSize >= opt.how_many:
            break

        # this is just a dictionary that contains tensors and stuff?
        generated = model(data_i, mode='inference')
        img_path = data_i['path']
        for b in range(generated.shape[0]):
            visualizer.save_images(img_path[b:b + 1], generated[b])


if __name__ == "__main__":
    run()

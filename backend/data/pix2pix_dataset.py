"""
Copyright (C) 2019 NVIDIA Corporation.  All rights reserved.
Licensed under the CC BY-NC-SA 4.0 license (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).
"""

from data.base_dataset import BaseDataset, get_params, get_transform
from PIL import Image
import util.util as util
import os


class Pix2pixDataset(BaseDataset):
    @staticmethod
    def modify_commandline_options(parser, is_train):
        # parser.add_argument('--no_pairing_check', action='store_true',
                            # help='If specified, skip sanity check of correct label-image file pairing')
        return parser

    def initialize(self, opt):
        self.opt = opt

        label_paths, instance_paths = self.get_paths(opt) #TODO modify

        util.natural_sort(label_paths)
        if not opt.no_instance: #TODO modify
            util.natural_sort(instance_paths)

        label_paths = label_paths[:opt.max_dataset_size] #TODO modify
        instance_paths = instance_paths[:opt.max_dataset_size] #TODO modify

        # NEVER sanity check 
        # if not opt.no_pairing_check:
        #     for path1, path2 in zip(label_paths, image_paths):
        #         assert self.paths_match(path1, path2), \
        #             "The label-image pair (%s, %s) do not look like the right pair because the filenames are quite different. Are you sure about the pairing? Please see data/pix2pix_dataset.py to see what is going on, and use --no_pairing_check to bypass this." % (path1, path2)

        self.label_paths = label_paths
        self.instance_paths = instance_paths

        size = len(self.label_paths)
        self.dataset_size = size
        # if opt.isTrain:
        #    round_to_ngpus = (size // ngpus) * ngpus
        #    self.dataset_size = round_to_ngpus

    def get_paths(self, opt):
        label_paths = []
        instance_paths = []
        assert False, "A subclass of Pix2pixDataset must override self.get_paths(self, opt)"
        return label_paths, instance_paths

    def paths_match(self, path1, path2):
        filename1_without_ext = os.path.splitext(os.path.basename(path1))[0]
        filename2_without_ext = os.path.splitext(os.path.basename(path2))[0]
        return filename1_without_ext == filename2_without_ext

    def __getitem__(self, index):
        # Label Image
        label_path = self.label_paths[index]
        label = Image.open(label_path)
        params = get_params(self.opt, label.size)
        transform_label = get_transform(
            self.opt, params, method=Image.NEAREST, normalize=False)
        label_tensor = transform_label(label) * 255.0

        # 'unknown' is opt.label_nc
        label_tensor[label_tensor == 255] = self.opt.label_nc

        # if using instance maps
        if self.opt.no_instance:
            instance_tensor = 0
        else:
            instance_path = self.instance_paths[index]
            instance = Image.open(instance_path)
            if instance.mode == 'L':
                instance_tensor = transform_label(instance) * 255
                instance_tensor = instance_tensor.long()
            else:
                instance_tensor = transform_label(instance)

        input_dict = {'label': label_tensor,
                      'instance': instance_tensor}

        # Give subclasses a chance to modify the final output
        self.postprocess(input_dict)

        return input_dict

    def postprocess(self, input_dict):
        return input_dict

    def __len__(self):
        return self.dataset_size

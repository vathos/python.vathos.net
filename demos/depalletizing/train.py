#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (c) 2021-2023, Vathos GmbH
#
# All rights reserved.
#
###############################################################################

import os
import pickle

import numpy as np

from vathos.authentication import get_service_account_token
from vathos.products import create_product
from vathos.services.depalletizing import train_product
from vathos.io.depth import read_from_png_uint8

if __name__ == '__main__':
  # authenticate with the API
  token = get_service_account_token(os.environ.get('CLIENT_ID'),
                                    os.environ.get('CLIENT_SECRET'))

  # define camera parameters
  projection_matrix = np.array(
      [[1779.80041, 0, 986.39929], [0, 1782.1018, 597.44458], [0, 0, 1]],
      dtype='f')
  image_size = (1944, 1200)
  image_range = (0.1, 2.0)  # in meters

  # create a product
  product_id = create_product('Python lib test',
                              './demos/depalletizing/cad_model.obj', 'mm',
                              projection_matrix, image_size, image_range, token)

  # save its id for inference later
  with open('product.pickle', 'wb') as fid:
    pickle.dump(product_id, fid)

  # read a calibration depth image from disk
  calibration_image = read_from_png_uint8(
      './demos/depalletizing/calibration.png')

  # start training
  train_product(product_id, calibration_image, token)

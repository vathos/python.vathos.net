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
from vathos.services.depalletizing import run_inference
from vathos.visualization import visualize_detections

if __name__ == '__main__':
  # authenticate with the API
  token = get_service_account_token(os.environ.get('CLIENT_ID'),
                                    os.environ.get('CLIENT_SECRET'))

  with open('./demos/depalletizing/product.pickle', 'rb') as fid:
    product_id = pickle.load(fid)

  detections = run_inference(product_id, './demos/depalletizing/test.png',
                             token)

  projection_matrix = np.array(
      [[1779.80041, 0, 986.39929], [0, 1782.1018, 597.44458], [0, 0, 1]],
      dtype='f')

  visualize_detections('./demos/depalletizing/cad_model.obj', 'mm',
                       './demos/depalletizing/test.png', projection_matrix,
                       detections)

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

  detections = run_inference(product_id,
                             './demos/depalletizing/test.png',
                             token,
                             score_threshold=0.9999,
                             refine_detections=True)

  visualize_detections(detections,
                       './demos/depalletizing/test.png',
                       token,
                       fitness_threshold=0.9)

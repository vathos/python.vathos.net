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
from pprint import pprint

import numpy as np

from vathos.authentication import get_service_account_token
from vathos.services.handeye import handeye_calibration

if __name__ == '__main__':
  # authenticate with the API
  token = get_service_account_token(os.environ.get('CLIENT_ID'),
                                    os.environ.get('CLIENT_SECRET'))

  # define camera parameters
  projection_matrix = np.array(
      [[1759.1642, 0, 962.8343], [0, 1764.0677, 595.8946], [0, 0, 1]],
      dtype='f')
  PATTERN_SIDELENGTH = 0.025
  PATTERN_SIZE = (10, 7)
  EYE_IN_HAND = True

  result = handeye_calibration('./demos/calibration/handeye/poses.csv',
                               projection_matrix, PATTERN_SIDELENGTH,
                               PATTERN_SIZE, EYE_IN_HAND, token)

  pprint(result)

# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2019-2023, Vathos GmbH
#
# All rights reserved.
#
################################################################################

import json
import logging
from time import perf_counter

import requests

from vathos.products import get_product
from vathos.configurations import get_configuration


def train_product(product_id, calibration_image_path, token):
  """Starts a training."""
  pass


def run_inference(product_id, test_image_path, token):
  """Runs an inference request."""
  product = get_product(product_id, token)
  configuration = get_configuration(product_id, 'votenet.workflows.vathos.net',
                                    token)

  # get depth image for visualization purposes and convert to m
  inference_url = 'https://staging.api.gke.vathos.net/v1/workflows/votenet'
  files = {'files': open(test_image_path, 'rb')}
  values = {
      'product': json.dumps(product),
      'configuration': json.dumps(configuration)
  }

  tic = perf_counter()
  inference_response = requests.post(
      inference_url,
      files=files,
      data=values,
      headers={'Authorization': 'Bearer ' + token},
      timeout=20)

  toc = perf_counter()
  logging.info('Inference took %f s', toc - tic)

  response_json = inference_response.json()

  return response_json['detections']

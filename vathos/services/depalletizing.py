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

from vathos import BASE_URL
from vathos.products import get_product
from vathos.configurations import get_configuration
from vathos.files import upload_files


def train_product(product_id, calibration_image_path, token, device_id=None):
  """Starts a training."""
  # upload calib image id
  calib_image = upload_files([calibration_image_path], token)[0]

  train_data = {
      'workflow':
          'votenet',
      'product':
          product_id,
      'device':
          device_id,
      'tasks': [{
          'service': 'extrinsic.calibration.vathos.net',
          'parameters': {
              'planeImage': calib_image['_id']
          }
      }, {
          'service': 'rendering.votenet.detection.vathos.net'
      }, {
          'service': 'train.votenet.detection.vathos.net'
      }, {
          'service': 'conversion.trt.vathos.net'
      }]
  }

  post_task_response = requests.post(
      f'{BASE_URL}/compositetasks',
      json=train_data,
      headers={'Authorization': f'Bearer {token}'},
      timeout=5)

  return post_task_response.json()['_id']


def run_inference(product_id, test_image_path, token):
  """Runs an inference request."""
  product = get_product(product_id, token)
  configuration = get_configuration(product_id, 'votenet.workflows.vathos.net',
                                    token)

  # get depth image for visualization purposes and convert to m
  inference_url = f'{BASE_URL}/workflows/votenet'
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

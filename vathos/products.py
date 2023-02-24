# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2019-2023, Vathos GmbH
#
# All rights reserved.
#
################################################################################
"""Product creation and administration."""

from time import sleep
import logging

import requests

from vathos.files import upload_files


def create_product(name, model_file_name, token):
  """Creates a product and attaches a 3d model file and camera to it."""
  # upload model file
  model_id = upload_files([model_file_name], token)[0]

  # create product
  post_product_response = requests.post(
      'https://staging.api.gke.vathos.net/v1/products',
      json={
          'name': name,
          'models': [model_id]
      },
      headers={'Authorization': f'Bearer {token}'},
      timeout=5)

  product = post_product_response.json()

  # run the model analysis task
  post_task_response = requests.post(
      'https://staging.api.gke.vathos.net/v1/tasks',
      json={
          'service': 'model.analysis.vathos.net',
          'product': product['_id']
      },
      headers={'Authorization': f'Bearer {token}'},
      timeout=5)
  task = post_task_response.json()

  # poll the task for completion
  while True:

    logging.debug('Waiting for task to finish...')
    sleep(5.0)
    task_status_request = requests.get(
        f'https://staging.api.gke.vathos.net/v1/tasks/{task["_id"]}',
        headers={'Authorization': f'Bearer {token}'},
        timeout=5)
    task_data = task_status_request.json()

    # break out of the loop as soon as the task is completed
    if task_data['status'] == 1:
      break
    elif task_data['status'] == -1:
      raise RuntimeError('Model post-processing failed')

  return product


def get_product(product_id, token):
  """Downloads product data."""
  url = f'https://staging.api.gke.vathos.net/v1/products/{product_id}?%24populate%5B0%5D=grips&%24populate%5B1%5D=states&%24populate%5B1%5D=camera'
  product_response = requests.get(url,
                                  headers={'Authorization': 'Bearer ' + token},
                                  timeout=5)
  return product_response.json()
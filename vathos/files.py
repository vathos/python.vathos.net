# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2019-2023, Vathos GmbH
#
# All rights reserved.
#
################################################################################
"""File operations."""

import requests


def upload_files(file_list, token):
  """Uploads one or multiple files."""
  upload_body = {}
  for i, file in enumerate(file_list):
    upload_body[f'file_{str(i).zfill(2)}'] = open(file, 'rb')
  upload_response = requests.post('https://staging.api.gke.vathos.net/v1/blobs',
                                  files=upload_body,
                                  headers={'Authorization': f'Bearer {token}'},
                                  timeout=120)
  return upload_response.json()

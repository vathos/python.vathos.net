# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2019-2023, Vathos GmbH
#
# All rights reserved.
#
################################################################################

import requests


def get_configuration(product_id, service, token):
  """Get the most recent inference configuration."""
  url = f'https://staging.api.gke.vathos.net/v1/configurations?product={product_id}&service={service}'
  response = requests.get(url,
                          headers={'Authorization': 'Bearer ' + token},
                          timeout=5)
  configurations = response.json()

  if len(configurations) == 0:
    return None
  else:
    # last is the newest
    return configurations[-1]['data']

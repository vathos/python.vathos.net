#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (c) 2021, Vathos GmbH
#
# All rights reserved.
#
###############################################################################

import os

from vathos.authentication import get_service_account_token
from vathos.products import get_product

if __name__ == '__main__':
  token = get_service_account_token(os.environ.get('CLIENT_ID'),
                                    os.environ.get('CLIENT_SECRET'))
  
  print(get_product('63f375eed312240012f01925', token))
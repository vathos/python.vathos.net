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

from vathos.authentication import get_service_account_token
from vathos.services.depalletizing import run_inference

if __name__ == '__main__':
  # authenticate with the API
  token = get_service_account_token(os.environ.get('CLIENT_ID'),
                                    os.environ.get('CLIENT_SECRET'))
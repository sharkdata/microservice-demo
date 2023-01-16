#!/usr/bin/python3
# -*- coding:utf-8 -*-

import demoapi_utils

__version__ = "2023.0.0-demo"
used_logger = "DemoAPILogger"

from demoapi_core.code_manager import CodeManager

# To be used similar to singleton objects.
logger = demoapi_utils.Logger(logger=used_logger)
config = demoapi_utils.Configuration(logger=used_logger)
manager = CodeManager(logger=used_logger)


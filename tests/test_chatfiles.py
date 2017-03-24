#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Hyphenate Inc'

import unittest
import json

import hyphenateserver.client.client as rest_client

from hyphenateserver.utils.types import *
from hyphenateserver.utils.loggers import Logger


class TestChatFilesServices(unittest.TestCase):
    logger = Logger.get_logger('TestEaseMobChatFilesServices.class')
    service_files = rest_client.get_instance(service_chatfiles)

    def test_upload_file(self):
        """upload file"""

        self.logger.info('------------test: upload file--------------------------------')

        resp = []
        try:
            file_path = 'tests/zjg.jpg'
            resp = self.service_files.upload_file(file_path)
            self.assertTrue(resp[0])
            self.logger.info('file uploading ok, response:' + json.dumps(resp[1]))
            self.logger.info('file uploading completed.\n')
        except AssertionError:
            self.logger.error('api:upload_file done, result:failed, ' +
                              'reason: ' + str(resp[1]['error_description']) + '\n')
            raise Exception('function: upload_file, result:failed, ' +
                            'reason: ' + str(resp[1]['error_description']))

    def test_download_file(self):
        """download file"""

        self.logger.info('------------test:download file--------------------------------')

        resp = []
        try:
            file_path = 'tests/zjg.jpg'
            local_file_path = '/tmp/zjg-1.jpg'
            resp = self.service_files.upload_file(file_path)
            self.assertTrue(resp[0])

            if resp[1] is not None:
                if 'entities' in resp[1]:
                    entity = resp[1]['entities'][0]
                    file_uuid = entity['uuid']

                    self.service_files.download_file(file_uuid, local_file_path)
                    self.logger.info('file downloaded, local file:' + local_file_path)
                    self.logger.info('file downloading completed.\n')
        except AssertionError:
            self.logger.error('downloading file done, result:failed, ' +
                              'reason: ' + str(resp[1]['error_description']) + '\n')
            raise Exception('function: download_file, result:failed, ' +
                            'reason: ' + str(resp[1]['error_description']))

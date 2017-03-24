#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Hyphenate Inc'


from hyphenateserver.utils.http_utils import http_get, http_post, file_upload, get_file_stream, http_put
from hyphenateserver.utils.file_utils import write
from hyphenateserver.utils.loggers import Logger


class EMIMUsersService(object):

    logger = Logger.get_logger('EMChatIMUsersService.class')

    def __init__(self, org, app, auth=None):
        self.org = org
        self.app = app
        self.auth = auth

    def create_new_user(self, payload):
        """regsiter IM user"""

        url = ('/%s/%s/users' % (self.org, self.app))
        return http_post(url, payload, self.auth)

    def im_user_login(self, payload):
        """user login"""

        url = ('/%s/%s/users' % (self.org, self.app))
        return http_post(url, payload)

    def query_users_by_username(self, username):
        """get a user"""

        url = ('/%s/%s/users/%s' % (self.org, self.app, username))
        return http_get(url, self.auth)

    def query_users(self, username):
        """get multiple users"""

        url = ('/%s/%s/users/%s' % (self.org, self.app, username))
        return http_get(url, self.auth)

    def modify_user_password(self, username, payload):
        """reset user's password"""

        url = ('/%s/%s/users/%s' % (self.org, self.app, username))
        return http_put(url, payload, self.auth)

    def modify_nickname(self, username, payload):
        """update user nickname"""

        url = ('/%s/%s/users/%s' % (self.org, self.app, username))
        return http_put(url, payload, self.auth)

    def query_offline_msg_count_of_user(self, username):
        """get number of offline messages"""

        url = ('/%s/%s/users/%s/offline_msg_count' % (self.org, self.app, username))
        return http_get(url, self.auth)

    def check_status_of_user(self, username):
        """get user online status"""

        url = ('/%s/%s/users/%s/status' % (self.org, self.app, username))
        return http_get(url, self.auth)

    def deactivate_user(self, username):
        """deactivate user account"""

        url = ('/%s/%s/users/%s/deactivate' % (self.org, self.app, username))
        return http_post(url, None, self.auth)

    def activate_user(self, username):
        """activate user account if deactivated"""

        url = ('/%s/%s/users/%s/activate' % (self.org, self.app, username))
        return http_post(url, None, self.auth)


class EMChatFilesService(object):

    logger = Logger.get_logger('EMChatFilesService.class')

    def __init__(self, org, app, auth=None):
        self.org = org
        self.app = app
        self.auth = auth

    def upload_file(self, file_path):
        """upload file"""

        url = ("/%s/%s/chatfiles" % (self.org, self.app))
        files = {'file': ('report.xls', open(file_path, 'rb'), 'image/jpeg', {'Expires': '0'})}
        return file_upload(url, files, self.auth)

    def download_file(self, file_uuid, local_file_path):
        """download file"""

        url = ("/%s/%s/chatfiles/%s" % (self.org, self.app, file_uuid))
        content = get_file_stream(url)

        write(local_file_path, content)


class EMMessagesService(object):

    logger = Logger.get_logger('EMChatMessagesService.class')

    def __init__(self, org, app, auth=None):
        self.org = org
        self.app = app
        self.auth = auth

    def send_messages(self, payload):
        url = ('/%s/%s/messages' % (self.org, self.app))
        return http_post(url, payload, self.auth)

#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Hyphenate Inc'


from hyphenate_server.utils.types import *
from hyphenate_server.services.emchat_service import *
from hyphenate_server.utils.confs import *


def get_instance(service_type):
    if service_type == service_users:
        return EMIMUsersService(org, app)
    if service_type == service_chatfiles:
        return EMChatFilesService(org, app)
    if service_type == service_messages:
        return EMMessagesService(org, app)

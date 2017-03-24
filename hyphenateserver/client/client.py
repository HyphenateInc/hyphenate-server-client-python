#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Hyphenate Inc'


from hyphenateserver.utils.types import *
from hyphenateserver.services.emchat_service import *
from hyphenateserver.utils.confs import *


def get_instance(service_type):
    if service_type == service_users:
        return EMIMUsersService(org, app)
    if service_type == service_chatfiles:
        return EMChatFilesService(org, app)
    if service_type == service_messages:
        return EMMessagesService(org, app)

#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hyphenate inc'

import requests
import json
from time import time
from requests.auth import AuthBase
import string
import random

JSON_HEADER = {'content-type': 'application/json'}
# HYPHENATE_HOST = "http://localhost:8080"#
HYPHENATE_HOST = "https://api.hyphenate.io"

DEBUG = False


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """generate random testing account"""
    return ''.join(random.choice(chars) for _ in range(size))


def parse_appkey(app_key):
    """parse API key to obtain org and app. API Key is constructed as {org}#{app}"""
    return tuple(app_key.split('#'))


def post(url, payload, auth=None):
    r = requests.post(url, data=json.dumps(payload), headers=JSON_HEADER, auth=auth)
    return http_result(r)


def get(url, auth=None):
    r = requests.get(url, headers=JSON_HEADER, auth=auth)
    return http_result(r)


def delete(url, auth=None):
    r = requests.delete(url, headers=JSON_HEADER, auth=auth)
    return http_result(r)


def http_result(r):
    if DEBUG:
        error_log = {
            "method": r.request.method,
            "url": r.request.url,
            "request_header": dict(r.request.headers),
            "response_header": dict(r.headers),
            "response": r.text
        }
        if r.request.body:
            error_log["payload"] = r.request.body
        print json.dumps(error_log)

    if r.status_code == requests.codes.ok:
        return True, r.json()
    else:
        return False, r.text


class Token:
    """authentication token"""

    def __init__(self, token, exipres_in):
        self.token = token
        self.exipres_in = exipres_in + int(time())

    def is_not_valid(self):
        """check validity and expiration (exipreis_in) of the authentication token
        current_time_in_seconds < (expires_in + token_acquired_time)
        """
        return time() > self.exipres_in


class HyphenateAuth(AuthBase):
    """handle login authentication"""

    def __init__(self):
        self.token = ""

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer ' + self.get_token()
        return r

    def get_token(self):
        """check the token obtained earlier to see if it's expired or not"""
        if (self.token is None) or (self.token.is_not_valid()):
            # refresh the token
            self.token = self.acquire_token()
        return self.token.token

    def acquire_token(self):
        """acquire a new token, method will return a token value"""
        pass


class AppClientAuth(HyphenateAuth):
    """Use the client_id and client_secret of the app to get app admin token"""

    def __init__(self, org, app, client_id, client_secret):
        super(AppClientAuth, self).__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.url = HYPHENATE_HOST + ("/%s/%s/token" % (org, app))
        self.token = None

    def acquire_token(self):
        """
        use client_id and client_secret to get token as the following REST API,
        POST /{org}/{app}/token {'grant_type':'client_credentials', 'client_id':'xxxx', 'client_secret':'xxxxx'}
        """
        payload = {'grant_type': 'client_credentials', 'client_id': self.client_id, 'client_secret': self.client_secret}
        success, result = post(self.url, payload)
        if success:
            return Token(result['access_token'], result['expires_in'])
        else:
            # throws exception
            pass


def register_new_user(org, app, auth, username, password):
    """register new Hyphenate user account
    POST /{org}/{app}/users {"username":"xxxxx", "password":"yyyyy"}
    """
    payload = {"username": username, "password": password}
    url = HYPHENATE_HOST + ("/%s/%s/users" % (org, app))
    return post(url, payload, auth)


def delete_user(org, app, auth, username):
    """remove user account
    DELETE /{org}/{app}/users/{username}
    """
    url = HYPHENATE_HOST + ("/%s/%s/users/%s" % (org, app, username))
    return delete(url, auth)


def upload_file(org, app, auth, file_path):
    """upload file
    curl --verbose --header "Authorization: Bearer YWMtz1hFWOZpEeOPpcmw1FB0RwAAAUZnAv0D7y9-i4c9_c4rcx1qJDduwylRe7Y" \
    --header "restrict-access:true" --form file=@/Users/stliu/a.jpg \
    http://api.hyphenate.io/hyphenatedemo/demo/chatfiles
    """
    url = HYPHENATE_HOST + ("/%s/%s/chatfiles" % (org, app))
    # files = {'file': open(file_path, 'rb')}
    files = {'file': ('report.xls', open(file_path, 'rb'), 'image/jpeg', {'Expires': '0'})}

    r = requests.post(url, files=files, auth=auth)
    return http_result(r)


if __name__ == '__main__':
    # testing case
    f = file("../info.json")
    s = json.load(f)
    test_app_key = s['appkey']
    org_name, app_name = parse_appkey(test_app_key)
    test_client_id = s['app']['credentials']['client_id']
    test_client_secret = s['app']['credentials']['client_secret']

    # use client id and secret to get app admin token
    app_client_auth = AppClientAuth(org_name, app_name, test_client_id, test_client_secret)
    print "Get app token with client id and secret: " + app_client_auth.get_token()

    print "now let's register some new users...."
    app_users = []
    for i in range(10):
        test_username = id_generator()

        test_password = '123456'
        test_success, test_result = register_new_user(org_name, app_name, app_client_auth, test_username, test_password)
        if test_success:
            print "registered new user %s with API key[%s]" % (test_username, test_app_key)
            app_users.append(test_username)
        else:
            print "failed to register new user %s in API key[%s]" % (test_username, test_app_key)

    print "now let's delete users just created, this time we're using app_client_auth"

    for test_username in app_users:
        test_success, test_result = delete_user(org_name, app_name, app_client_auth, test_username)
        if test_success:
            print "user[%s] is deleted from API key[%s]" % (test_username, test_app_key)
        else:
            print "failed to delete user[%s] from API key[%s]" % (test_username, test_app_key)

    print "now let's send an image"
    test_success, test_result = upload_file(org_name, app_name, app_client_auth, '../tests/zjg.jpg')

    print test_result

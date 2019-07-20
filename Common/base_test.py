import unittest
import requests
import json
from Logs.log import log1
import getcwd
import os
import configparser

path = getcwd.get_cwd()
config_path = os.path.join(path, 'Config/config.ini')


class WebRequests(unittest.TestCase):

    @staticmethod
    def get(url, params=None, headers=None, files=None):
        # return response code and content #
        try:
            r = requests.get(url, params=params, headers=headers, files=files)
            log1.info("request content：%s" % params)
            status_code = r.status_code  # status code
            log1.info("get status code:%d" % status_code)
            response_json = r.json()  # response content
            log1.info("response content：%s" % response_json)
            return status_code, response_json
        except BaseException as e:
            log1.error("request fail！", exc_info=1)

    @staticmethod
    def post(url, data=None, headers=None, files=None):
        # return response code and content #
        try:
            r = requests.post(url, data=data, headers=headers, files=files)
            log1.info("requests content：%s" % data)
            status_code = r.status_code
            log1.info("status code:%d" % status_code)
            response_json = r.json()
            log1.info("response content：%s" % response_json)
            return status_code, response_json  # return response code and content #

        except BaseException as e:
            log1.error("requests fail", exc_info=1)

    @staticmethod
    def post_json(url, data=None, headers=None):
        # send value via json，return response code and content
        try:
            data = json.dumps(data).encode('utf-8')
            r = requests.post(url, data=data, headers=headers)
            log1.info("requests content：%s" % data)
            status_code = r.status_code  # response code
            log1.info("status code:%d" % status_code)
            response = r.json()
            log1.info("response content：%s" % response)
            return status_code, response  # return response code and content
        except BaseException as e:
            log1.error("request fail！", exc_info=1)

    @staticmethod
    def confige_get(session, key):
        config = configparser.ConfigParser()
        config.read(config_path, encoding="utf-8-sig")
        return config.get(session, key)

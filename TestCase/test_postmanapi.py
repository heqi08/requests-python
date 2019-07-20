import unittest
from Logs.log import log1
from Common.base_test import WebRequests


class PostmanTest(unittest.TestCase):

    def test_timestamp_before_target(self):
        case_name = 'timestamp before target'
        log1.info("Execution case：%s" % case_name)
        postapi = WebRequests()
        url = postapi.confige_get('test', 'url')
        payload = {'timestamp': '2016-10-10', "target": "2017-10-10"}
        status_code, response_json = postapi.get(url, params=payload)
        self.assertEqual(status_code, 200)
        self.assertEqual(response_json, {'before': True})

    def test_timestamp_after_target(self):
        case_name = 'timestamp after target'
        log1.info("Execution case：%s" % case_name)
        postapi = WebRequests()
        url = postapi.confige_get('test', 'url')
        payload = {'timestamp': '2018-10-10', "target": "2017-10-10"}
        status_code, response_json = postapi.get(url, params=payload)
        self.assertEqual(status_code, 200)
        self.assertEqual(response_json, {'before': False})

    def test_timestamp_equal_target(self):
        case_name = 'timestamp equal target'
        log1.info("Execution case：%s" % case_name)
        postapi = WebRequests()
        url = postapi.confige_get('test', 'url')
        payload = {'timestamp': '2018-10-10', "target": "2017-10-10"}
        status_code, response_json = postapi.get(url, params=payload)
        self.assertEqual(status_code, 200)
        self.assertEqual(response_json, {'before': False})

    def test_invalid_timestamp_and_target(self):
        case_name = 'timestamp equal target'
        log1.info("Execution case：%s" % case_name)
        postapi = WebRequests()
        url = postapi.confige_get('test', 'url')
        payload = {'timestamp': '2018-2-30', "target": "2017-10-10"}
        status_code, response_json = postapi.get(url, params=payload)
        self.assertEqual(status_code, 400)

    def test_timestamp_close_target(self):
        case_name = 'timestamp equal target'
        log1.info("Execution case：%s" % case_name)
        postapi = WebRequests()
        url = postapi.confige_get('test', 'url')
        payload = {'timestamp': '2017-10-9', "target": "2017-10-10"}
        status_code, response_json = postapi.get(url, params=payload)
        self.assertEqual(status_code, 200)
        self.assertEqual(response_json, {'before': True})


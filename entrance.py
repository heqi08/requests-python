import TestCase.test_postmanapi
import HTMLReport
import getcwd
import os

import unittest

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCase.test_postmanapi.PostmanTest('test_timestamp_before_target'))
    suite.addTest(TestCase.test_postmanapi.PostmanTest('test_timestamp_after_target'))
    suite.addTest(TestCase.test_postmanapi.PostmanTest('test_invalid_timestamp_and_target'))
    suite.addTest(TestCase.test_postmanapi.PostmanTest('test_timestamp_equal_target'))
    suite.addTest(TestCase.test_postmanapi.PostmanTest('test_timestamp_close_target'))
    path = getcwd.get_cwd()
    runner = HTMLReport.TestRunner(
        title='POSTMAN API test',
        description='TW homework api automation test',
        lang='en'
    )
    runner.run(suite)

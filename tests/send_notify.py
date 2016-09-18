#!/usr/bin/env python3

import unittest
import wtl
import os
import requests

class SendNotifyTests(unittest.TestCase):

    def test_no_config_is_none(self):
        self.assertRaises(ValueError, wtl.send_notify, {}, "test", None)

    def test_no_config(self):
        self.assertRaises(ValueError, wtl.send_notify, {}, "test", {})

    def test_config_none(self):
        config = {
            'protocol':None,
            'hostname':None,
            'port':None,
            'token':None,
            'service':None,
        }
        self.assertRaises(ValueError, wtl.send_notify, {}, "test", config)

    def test_InvalidSchema(self):
        config = {
            'protocol':"test",
            'hostname':"test",
            'port':0,
            'token':"test",
            'service':"test",
        }
        self.assertRaises(requests.exceptions.InvalidSchema, wtl.send_notify, {}, "test", config)

if __name__ == '__main__':
    unittest.main()

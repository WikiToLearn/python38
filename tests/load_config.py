#!/usr/bin/env python3

import unittest
import wtl
import os

class LoadConfigTests(unittest.TestCase):

    def test_config_not_found(self):
        config = wtl.load_config(config_dir=os.getcwd()+"/dirnotfound/")
        self.assertEqual(config, None)

    def test_config(self):
        config = wtl.load_config(config_prefix="a",config_dir=os.getcwd()+"/configs/")
        self.assertEqual(config, [{'a':'b'}])

    def test_config_default(self):
        config = wtl.load_config(config_prefix="b",config_dir=os.getcwd()+"/configs/")
        self.assertEqual(config, [{'b':'a'}])

if __name__ == '__main__':
    unittest.main()

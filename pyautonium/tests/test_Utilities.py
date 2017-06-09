import unittest

import Utilities as utils
import sendMail


class TestUtils(unittest.TestCase):

    def test_add_three(self):
        self.assertEqual(utils.activeWindow(), None)

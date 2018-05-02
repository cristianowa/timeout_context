import unittest
from time import sleep
from timeout_context import Timeout, TimeoutException


class TestTimeoutContext(unittest.TestCase):
    def test_works(self):
        x = False
        with Timeout(3):
            sleep(2)
            x = True
        self.assertTrue(x)

    def test_raises(self):
        with self.assertRaises(TimeoutException):
            with Timeout(1):
                sleep(2)
    def test_multiple(self):
        x = False
        with Timeout(1):
            x = True
        self.assertTrue(x)
        with self.assertRaises(TimeoutException):
            with Timeout(1):
                sleep(2)



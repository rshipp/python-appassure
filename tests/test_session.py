import unittest
try:
    from mock import Mock
except ImportError:
    from unittest.mock import Mock

from appassure.session import AppAssureSession

class TestSession(unittest.TestCase):

    def setUp(self):
        pass

import unittest
try:
    from mock import Mock
except ImportError:
    from unittest.mock import Mock

from appassure.session import AppAssureSession

class TestSession(unittest.TestCase):

    def setUp(self):
        pass

    def test_supports_context_manager(self):
        try:
            with AppAssureSession(None, None, None, None) as a:
                pass
        except AttributeError:
            self.fail()


import unittest
import datetime
from appassure import time

class TestTime(unittest.TestCase):
    
    def setUp(self):
        self.timeobj = datetime.datetime(2010, 1, 2, 3, 4, 5, 123000)
        self.timestr = '2010-01-02T03:04:05'
        self.timeapi = '2010-01-02T03:04:05.123Z'
        self.timehum = '2010-01-02 03:04:05'
    
    def test_formatTime(self):
        assert time.formatTime(self.timeobj) == self.timestr

    def test_deformatTime(self):
        assert time.deformatTime(self.timeapi) == self.timeobj

    def test_reformatTime(self):
        assert time.reformatTime(self.timeapi) == self.timehum

import unittest
from collections import OrderedDict
from appassure import api

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.api = api.AppAssureAPI(None)
        self.xml = '<?xml version="1.0" encoding="utf-8"?>'
        self.xmlns = 'xmlns="http://apprecovery.com/management/api/2010/05"'
        self.nonetag = self.xml + '<None ' + self.xmlns

    def test_supports_context_manager(self):
        try:
            with api.AppAssureAPI(None) as a:
                pass
        except AttributeError:
            self.fail()

    def test_none_is_none(self):
        self.assertEqual(self.api.getXML(''), self.nonetag + '></None>')

    def test_tag_is_tag(self):
        self.assertEqual(self.api.getXML('', 'tag'), self.xml + '<tag ' + \
            self.xmlns + '></tag>')

    def test_string_is_string(self):
        self.assertEqual(self.api.getXML('string'),
                self.nonetag + '>string</None>')

        self.assertEqual(self.api.getXML('<string></string>'), self.nonetag + \
            '><string></string></None>')

        self.assertEqual(self.api.getXML('<string>str</string>'), self.nonetag + \
            '><string>str</string></None>')

    def test_list_is_list(self):
        self.assertEqual(self.api.getXML(['item']),
                self.nonetag + '>item</None>')

        self.assertEqual(self.api.getXML(['item1', 'item2']), self.nonetag + \
            '>item1</None><None ' + self.xmlns + '>item2</None>')

    def test_dict_is_dict(self):
        self.assertEqual(self.api.getXML({'key': 'value'}), self.nonetag + \
            '><key>value</key></None>')

        xml = self.api.getXML({'key1': 'value1', 'key2': 'value2'})
        assert(xml == self.nonetag + '><key1>value1</key1><key2>value2</key2></None>' or \
               xml == self.nonetag + '><key2>value2</key2><key1>value1</key1></None>')

        self.assertEqual(self.api.getXML({'key': {'nestedkey': 'value'}}), self.nonetag + \
            '><key><nestedkey>value</nestedkey></key></None>')

        self.assertEqual(self.api.getXML({'key': ['item1', 'item2']}), self.nonetag + \
            '><key>item1</key><key>item2</key></None>')

    def test_ordereddict_is_ordereddict(self):
        ordereddict = OrderedDict([
                ('key1', 'value1'),
                ('key2', 'value2'),
                ('key3', ['item1', 'item2'])
        ])
        orderedxml = self.nonetag + '><key1>value1</key1><key2>value2</key2>' + \
            '<key3>item1</key3><key3>item2</key3></None>'
        self.assertEqual(self.api.getXML(ordereddict), orderedxml)

    def test_xmlns_is_xmlns(self):
        self.assertEqual(self.api.getXML('', 'tag xmlns="ns"'), self.xml + \
            '<tag xmlns="ns" ' + self.xmlns + '></tag>')

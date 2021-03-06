"""This is a dummy template file that shows how an actual AppAssureAPI
subclass should be implemented. Each subclass should contain one of
the AppAssure Core API interfaces listed here:
http://docs.appassure.com/display/AA50D/Core+API+Reference

Note that you should never need to override the __init__ function.
"""

from appassure.api import AppAssureAPI

class ITemplate(AppAssureAPI):

    def getExampleData(self):
        """Gets example data."""
        return self.session.request('templateuri')

    def doSomethingOnTheServer(self):
        """Does something on the server."""
        data = {
            'mykey': {
                'insidekey': 'yay!',
                'doublekey': {
                    'moreKeys': 'value!!!'
                },
            },
            'wrapmeinTemplateTag': 'please',
        }

        # Send the following xml data to the server:
        # <?xml version="1.0" encoding="utf-8"?>
        # <TemplateTag xmlns="blah"><wrapmeinTamplateTag>please
        # </wrapmeinTemplateTag><mykey><insidekey>yay!</insidekey>
        # <doublekey><moreKeys>value!!!</moreKeys></doublekey>
        # </mykey></TemplateTag>
        return self.session.request('dosomethinguri', 'POST',
                self.getXML(data, 'TemplateTag'))

"""AppAssure 5 REST API"""

from appassure.appassureapi import AppAssureAPI

class IExchangeManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/pages/viewpage.action?pageId=2294029
    """

    def getExchangeDllInfo(self, fileName):
        """Gets information about MS Exchange library."""
        return self.session.request('exchangedll/%s/'
                % (fileName))

    def startNewFileTransmitSession(self, data):
        """Starts new file transmit session."""
        return self.session.request('exchangedll/newsession/', 'POST',
                    self.getXML(data, 'fileTransmitRequest'))

    def endTransmitFile(self, fileTransmitSessionId):
        """Ends current transmit session."""
        return self.session.request('exchangedll/sessions/%s/'
                % (fileTransmitSessionId), 'POST')

    def cancelTransmitFile(self, fileTransmitSessionId):
        """Cancels current transmit session."""
        return self.session.request('exchangedll/sessions/%s/'
                % (fileTransmitSessionId))

    def continueTransmitFile(self, fileTransmitSessionId, bytesToRead):
        """Reads data from agent in current transmit session."""
        return self.session.request('exchangedll/sessions/%s/data/%s'
                % (fileTransmitSessionId, bytesToRead), 'POST')

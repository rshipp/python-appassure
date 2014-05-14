"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IReplayEngineManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IReplayEngineManagement
    """

    def getConfiguration(self):
        """Retrieves the current configuration of the Replay
        Engine service.
        """
        return self.session.request('replayEngine/config')

    def setConfiguration(self, data):
        """Sets the configuration of the service."""
        return self.session.request('replayEngine/config', 'POST',
                    self.getXML(data, 'replayEngineConfig'))

    def getConnections(self):
        """Gets a list of the active connections to the Replay
        Engine service.
        """
        return self.session.request('replayEngine/connections')

    def closeConnection(self, id):
        """Forcibly closes an existing connection to the
        AppAssure 5 Engine.
        """
        return self.session.request('replayEngine/connections/%s'
                % (id))

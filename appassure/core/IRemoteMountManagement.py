"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IRemoteMountManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IRemoteMountManagement
    """

    def addRemoteMount(self, data):
        """Add information about remote mount point."""
        return self.session.request('remoteMounts/addRemoteMount', 'POST',
                    self.getXML(data, 'remoteMountRequest'))

    def disconnect(self, remoteMountItemId, mountType):
        """Disconnect remote mount point."""
        return self.session.request('remoteMounts/disconnect/%s/mountType/%s'
                % (remoteMountItemId, mountType), 'POST')

    def disconnectAll(self):
        """Disconnect all remote mount points."""
        return self.session.request('remoteMounts/disconnectAll', 'POST')

    def disconnectAllForAgent(self, agentId):
        """Disconnect all remote mount points for particular agent."""
        return self.session.request('remoteMounts/disconnectAllForAgent/%s'
                % (agentId), 'POST')

    def getAgentRemoteMounts(self, agentId):
        """Gets information about remote mount points for
        particular agent.
        """
        return self.session.request('remoteMounts/getAgentRemoteMoutns/%s'
                % (agentId), 'POST')

    def getRemoteMounts(self):
        """Gets information about remote mount points."""
        return self.session.request('remoteMounts/remoteMountInfos', 'POST')

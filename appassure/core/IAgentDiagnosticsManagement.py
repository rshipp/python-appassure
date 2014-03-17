"""AppAssure 5 Core API"""

from appassure.appassureapi import AppAssureAPI

class IAgentDiagnosticsManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IAgentDiagnosticsManagement
    """

    def executeRemoteCommand(self, data, agentId):
        """Executes an arbitrary remote command."""
        return self.session.request('agentdiag/%s/command/'
                % (agentId), 'POST',
                    self.getXML(data, 'remoteCommand'))

    def getLog(self, agentId):
        """Gets the entire contents of the replay.log file."""
        return self.session.request('agentdiag/%s/log/'
                % (agentId))

    def uploadLogSessions(self, agentId):
        """Uploads the current log session to Gibraltar.
        (http:// www.gibraltarsoftware.com/)
        """
        return self.session.request('agentdiag/%s/log/'
                % (agentId), 'POST')

    def restartService(self, agentId):
        """Stops, forcibly kills (if necessary), and
        re-starts the service.
        """
        return self.session.request('agentdiag/%s/service/'
                % (agentId), 'DELETE')

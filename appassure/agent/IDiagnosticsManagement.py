"""AppAssure 5 REST API"""

from appassure.appassureapi import AppAssureAPI

class IDiagnosticsManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/pages/viewpage.action?pageId=2294037
    """

    def executeRemoteCommand(self, data):
        """Executes an arbitrary remote command."""
        return self.session.request('diag/command/', 'POST',
                    self.getXML(data, 'remoteCommand'))

    def readFile(self, path):
        """Reads a file from the local file system and streams it
        back to the client.
        """
        return self.session.request('diag/files/?q=%s'
                % (path))

    def getLog(self):
        """Gets the entire contents of the replay.log file."""
        return self.session.request('diag/log/')

    def getLogSession(self):
        """Packages the current log session and returns it as a
        byte stream. The contents of the stream is a Gibraltar .glp file.
        """
        return self.session.request('diag/logSession/')

    def uploadLogSessions(self):
        """Uploads the current log session to the Gibraltar
        (http:// www.gibraltarsoftware.com/) logging framework.
        """
        return self.session.request('diag/logSession/', 'POST')

    def restartService(self):
        """Stops, forcibly kills (if necessary), and re-starts
        the service.
        """
        return self.session.request('diag/service/')

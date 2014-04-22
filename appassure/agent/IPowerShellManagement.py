"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IPowerShellManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IPowerShellManagement
    """

    def runPowerShellScriptFromFile(self, data):
        """Runs PowerShell script on the agent."""
        return self.session.request('powerShell/', 'POST',
                    self.getXML(data, 'runPowerShellScriptRequest'))

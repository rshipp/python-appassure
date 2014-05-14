"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class ILogTruncationManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ILogTruncationManagement
    """

    def forceLogTruncation(self, data, agentId):
        """Forces a log truncation job for the specified agent."""
        return self.session.request('logtruncation/agents/%s/force'
                % (agentId), 'POST',
                    self.getXML(data, 'TargetComponentTypes'))

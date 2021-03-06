"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IStatusSummaryManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IStatusSummaryManagement
    """

    def getCoreEventsInfo(self, data):
        """Gets core events info such as events, jobs etc."""
        return self.session.request('status/coreEventsInfo', 'POST',
                    self.getXML(data, 'coreEventsInfoRequest'))

    def getCoreHomeInfo(self):
        """Gets core metadata and recent 10 alerts."""
        return self.session.request('status/coreHomeInfo')

    def getCoreSystemInfo(self):
        """Gets core system info such as mounts, metadata,
        settings, repository configuration etc.
        """
        return self.session.request('status/coreSystemInfo')

    def crash(self):
        """Crashes the process."""
        return self.session.request('status/crash')

    def getDashboardInfo(self):
        """Get the status info necessary to display the dashboard
        on the main screen.
        """
        return self.session.request('status/dashboard')

    def getAgentDashboardInfo(self, agentId):
        """Get the status info for a specific Agent."""
        return self.session.request('status/dashboard/%s'
                % (agentId))

    def getFailedServicesInfo(self):
        """Gets names of services failed to initialize."""
        return self.session.request('status/failedServicesInfo')

    def getLatestEvents(self):
        """Gets latest core events info such as events
        accumulated since last call to itself or start of core if call
        is first.
        """
        return self.session.request('status/latestEventsInfo')

    def retryStartFailedServices(self):
        """Tries to restart failed services."""
        return self.session.request('status/restart/', 'POST')

    def getStatusSummary(self):
        """Get a summary of the status of all services including
        in the status summary API.
        """
        return self.session.request('status/statusSummary')

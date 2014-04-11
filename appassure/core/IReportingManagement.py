"""AppAssure 5 Core API"""

from appassure.appassureapi import AppAssureAPI

class IReportingManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IReportingManagement
    """

    def getAgentFailureReport(self, data):
        """Gets a failure report for a particular agent."""
        return self.session.request('report/agentFailureReport', 'PUT',
                    self.getXML(data, 'agentReportRequest'))

    def getAgentReport(self, data):
        """Gets a report for a particular agent."""
        return self.session.request('report/agentReport', 'PUT',
                    self.getXML(data, 'agentReportRequest'))

    def getCoreFailureReport(self, data):
        """Gets a failure report for a particular set of cores."""
        return self.session.request('report/coreFailureReport', 'PUT',
                    self.getXML(data, 'coreReportRequest'))

    def getCoreReport(self, data):
        """Gets a report for a particular set of cores."""
        return self.session.request('report/coreReport', 'PUT',
                    self.getXML(data, 'coreReportRequest'))

    def getDatabaseCoreIdentities(self):
        """Gets identity (id-name pairs) of Cores having
        reporting data in database currently used by the Core.
        """
        return self.session.request('report/databaseCoreIdentities')

    def getSelfReport(self, data):
        """Gets a report for this core."""
        return self.session.request('report/selfReport', 'PUT',
                    self.getXML(data, 'selfReportRequest'))

    def getSummaryReport(self, data):
        """Gets a summary report for this core."""
        return self.session.request('report/summaryReport', 'PUT',
                    self.getXML(data, 'summaryReportRequest'))

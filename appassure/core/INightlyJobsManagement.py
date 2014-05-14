"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class INightlyJobsManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/INightlyJobsManagement
    """

    def cancelNightlyJobs(self):
        """Cancels all nightly jobs execution."""
        return self.session.request('nightlyJobs/')

    def getNightlyJobsSettings(self):
        """Gets nightly jobs settings for the Core."""
        return self.session.request('nightlyJobs/config')

    def setNightlyJobsSettings(self, data):
        """Sets nightly jobs settings for the Core."""
        return self.session.request('nightlyJobs/config', 'PUT',
                    self.getXML(data, 'nightlyJobsSettings'))

    def getAgentNightlyJobs(self, agentId):
        """Gets jobs for the specified agent."""
        return self.session.request('nightlyJobs/config/%s'
                % (agentId))

    def setAgentNightlyJobs(self, data, agentId):
        """Sets enabled nightly jobs for the agent."""
        return self.session.request('nightlyJobs/config/%s'
                % (agentId), 'PUT',
                    self.getXML(data, 'nightlyJobIds'))

    def setJobConfiguration(self, jobId):
        """Sets job configuration."""
        return self.session.request('nightlyJobs/jobConfiguration/%s'
                % (jobId), 'PUT')

    def getJobConfiguration(self, jobId):
        """Gets job configuration for the specified job."""
        return self.session.request('nightlyJobs/jobConfiguration/%s'
                % (jobId))

    def setAgentJobConfiguration(self, jobId, agentId):
        """Sets job configuration for specified agent."""
        return self.session.request('nightlyJobs/jobConfiguration/%s/%s'
                % (jobId, agentId), 'PUT')

    def getAgentJobConfiguration(self, jobId, agentId):
        """Gets job configuration for the specified job of the
        agent.
        """
        return self.session.request('nightlyJobs/jobConfiguration/%s/%s'
                % (jobId, agentId))

    def getNightlyJobsStatus(self):
        """Determines whether nightly jobs are in progress and
        then gets the transaction id of currently running jobs.
        """
        return self.session.request('nightlyJobs/status')

"""AppAssure 5 Core API"""

from appassure.appassureapi import AppAssureAPI

class IBackgroundJobManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IBackgroundJobManagement
    """

    def getJobsForAgentByPage(self, agentId, page):
        """Gets the current list of jobs for a specific 
        agent, such that the results are paged for easy viewing in a 
        paged grid in GUI.
        """
        return self.session.request('jobmgr/agents/%s/jobs/paged?filter=%s&max=%s&page=%s' 
                % (agentId, page))

    def getAllJobsForAgentCount(self, agentId, filter):
        """Gets the current number of jobs, in memory and 
        database, for a specific agent.
        """
        return self.session.request('jobmgr/agents/%s/jobsCount?filter=%s' 
                % (agentId, filter))

    def cancelChildJob(self, parentJobId, childJobId):
        """Cancels the child job."""
        return self.session.request('jobmgr/jobs/%s/childJobs/%s' 
                % (parentJobId, childJobId), 'DELETE')

    def getJob(self, jobId):
        """Gets the specified job."""
        return self.session.request('jobmgr/jobs/%s' 
                % (jobId))

    def cancelJob(self, jobId):
        """Cancels the job."""
        return self.session.request('jobmgr/jobs/%s' 
                % (jobId), 'DELETE')

    def updateJobRequest(self, data, jobId):
        """Updates the specified job."""
        return self.session.request('jobmgr/jobs/%s' 
                % (jobId), 'POST', 
                    self.getXML(data, 'backgroundJobRequest'))

    def getCoreJobsByPage(self, page):
        """Gets the current list of jobs for the core, such 
        that the results are paged for easy viewing in a paged grid.
        """
        return self.session.request('jobmgr/jobs/core/paged?filter=%s&max=%s&page=%s' 
                % (page))

    def getAllJobsCount(self, filter):
        """Gets the current number of jobs, in memory and 
        database.
        """
        return self.session.request('jobmgr/jobsCount?filter=%s' 
                % (filter))

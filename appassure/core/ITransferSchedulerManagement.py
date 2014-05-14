"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class ITransferSchedulerManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ITransferSchedulerManagement
    """

    def getActualAgentProtectionConfiguration(self, agentId):
        """Gets the actual protection groups configured for the
        agent.
        """
        return self.session.request('xfer/schedule/%s/actualProtectionConfiguration'
                % (agentId))

    def getAgentConfiguration(self, agentId):
        """Gets the transfer configuration settings for the agent."""
        return self.session.request('xfer/schedule/%s/config'
                % (agentId))

    def setAgentConfiguration(self, data, agentId):
        """Sets the transfer configuration settings for the agent."""
        return self.session.request('xfer/schedule/%s/config'
                % (agentId), 'PUT',
                    self.getXML(data, 'xferConfig'))

    def getCachedAgentProtectionConfiguration(self, agentId):
        """Gets the cached protection groups configured for the
        agent.
        """
        return self.session.request('xfer/schedule/%s/pgs'
                % (agentId))

    def setAgentProtectionConfiguration(self, data, agentId):
        """Sets the protection groups configured for the agent."""
        return self.session.request('xfer/schedule/%s/pgs'
                % (agentId), 'PUT',
                    self.getXML(data, 'protectionConfig'))

    def forceTransfer(self, data, agentId):
        """Forces an immediate transfer of the specified
        protection group.
        """
        return self.session.request('xfer/schedule/%s/transfer'
                % (agentId), 'POST',
                    self.getXML(data, 'forceTransfer'))

    def batchAgentsProtectionPaused(self, data):
        """         Summary:."""
        return self.session.request('xfer/schedule/agentsPaused', 'POST',
                    self.getXML(data, 'batchAgentsProtectionPausedRequest'))

    def batchAgentsProtectionResumed(self, data):
        """         Summary:."""
        return self.session.request('xfer/schedule/agentsResumed', 'POST',
                    self.getXML(data, 'batchAgentsProtectionPausedRequest'))

    def applyRepositoryToUnprotectedAgents(self, repositoryName):
        """         Summary:."""
        return self.session.request('xfer/schedule/applyrepository/%s'
                % (repositoryName), 'PUT')

    def forceAllTransfer(self, data):
        """Forces an immediate transfer for all available agents."""
        return self.session.request('xfer/schedule/forcealltransfer', 'POST',
                    self.getXML(data, 'forceTransfer'))

    def removeRepositoryFromProtection(self, repositoryName):
        """         Summary:."""
        return self.session.request('xfer/schedule/removerepository/%s'
                % (repositoryName))

    def getScheduleTemplates(self):
        """Gets the transfer schedule templates collection."""
        return self.session.request('xfer/schedule/transferScheduleTemplates')

    def addScheduleTemplate(self, data):
        """Adds new transfer schedule template."""
        return self.session.request('xfer/schedule/transferScheduleTemplates', 'POST',
                    self.getXML(data, 'transferScheduleTemplate'))

    def getScheduleTemplate(self, templateId):
        """Gets the transfer schedule template by id."""
        return self.session.request('xfer/schedule/transferScheduleTemplates/%s'
                % (templateId))

    def updateScheduleTemplate(self, data, templateId):
        """Updates existing transfer schedule template."""
        return self.session.request('xfer/schedule/transferScheduleTemplates/%s'
                % (templateId), 'PUT',
                    self.getXML(data, 'transferScheduleTemplate'))

    def deleteScheduleTemplate(self, templateId):
        """Removes transfer schedule template."""
        return self.session.request('xfer/schedule/transferScheduleTemplates/%s'
                % (templateId))

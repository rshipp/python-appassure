"""AppAssure 5 Core API"""

from appassure.appassureapi import AppAssureAPI

class IRecoveryPointsManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IRecoveryPointsManagement
    """

    def deleteRecoveryPointsForAgent(self, agentId):
        """Deletes all recovery points for specified agent."""
        return self.session.request('recoveryPoints/agents/%s'
                % (agentId), 'DELETE')

    def getAllRecoveryPoints(self, agentId):
        """Gets the summary information for all recovery
        points associated with the specified agent. Note that this
        list can potentially be very large.
        """
        return self.session.request('recoveryPoints/agents/%s/all'
                % (agentId))

    def startCheckAgentRecoveryPoints(self, agentId, fixErrors):
        """Starts a task that performs integrity check of all
        agent's recovery points and tries to fix errors being found
        """
        return self.session.request('recoveryPoints/agents/%s/integritycheck/fix?fixErrors=%s'
                % (agentId, fixErrors))

    def getRecoveryPointsByPage(self, agentId, page):
        """Gets summary info for recovery points for a given
        agent ID, such that the results are paged for easy viewing
        in a paged grid.
        """
        return self.session.request('recoveryPoints/agents/%s/paged?max=%s&page=%s'
                % (agentId, page))

    def getRecoveryPoints(self, agentId):
        """Gets the summary information for the recovery
        points associated with a specified agent that fall outside
        of a last modified date/time range. You also specify a
        maximum number of recovery points to return with the
        specified range. {olderThan}&newerThan={newerThan}
        """
        return self.session.request('recoveryPoints/agents/%s/where?max=%s&olderThan='
                % (agentId))

    def mergeAgentRecoveryPoints(self, data, sourceAgentId):
        """Merges the recovery points of the agent ID
        identified by the URI into another agent ID specified in the
        request.
        """
        return self.session.request('recoveryPoints/agents/%s'
                % (sourceAgentId), 'POST',
                    self.getXML(data, 'mergeRecoveryPointsRequest'))

    def getAgentsRecoveryPointsInfo(self):
        """Gets a list of all agents with recovery points."""
        return self.session.request('recoveryPoints/agents/all')

    def getVolumeImageDetails(self, imageId):
        """'Gets information for a single volume image
        specified by unique identifier.
        """
        return self.session.request('recoveryPoints/images/%s/'
                % (imageId))

    def getImageRawData(self):
        """Gets a stream of data consisting of the data in
        the image at the specified offset and length. Useful only
        for diagnostic purposes.
        """
        return self.session.request('recoveryPoints/images/rawdata/%s.rawdata?blockOffset='
                % ())

    def getImageRawKeys(self, imageId.rawkeys):
        """Gets a stream of offset/key pairs, containing the
        block offsets in the image and the DVM keys of the record at
        each block offset. Useful only for diagnostic purposes.
        """
        return self.session.request('recoveryPoints/images/rawkeys/%s.rawkeys'
                % (imageId.rawkeys))

    def getImageRawKeysText(self, imageId.textkeys):
        """Gets a stream of offset/key pairs, containing the
        block offsets in the image and the DVM keys of the record at
        each block offset. Useful only for diagnostic purposes.
        """
        return self.session.request('recoveryPoints/images/rawkeys/%s.textkeys'
                % (imageId.textkeys))

    def getMostRecentRecoveryPoints(self, data):
        """Gets summary info for the most recent recovery
        point of every agent specified in the request.
        """
        return self.session.request('recoveryPoints/recent', 'PUT',
                    self.getXML(data, 'getMostRecentRecoveryPoints'))

    def deleteRecoveryPointsRange(self, data):
        """Deletes all recovery points in a specified time
        period for the specified agent.
        """
        return self.session.request('recoveryPoints/rps/deleteRecoveryPointsRange', 'POST',
                    self.getXML(data, 'adHocDeleteRecoveryPointsRequest'))

    def deleteRecoveryPointsChain(self, recoveryPointId):
        """Deletes all volume image chains that contain
        volume images for a given recovery point.
        """
        return self.session.request('recoveryPoints/rps/%s'
                % (recoveryPointId), 'DELETE')

    def getRecoveryPointDetails(self, recoveryPointId):
        """Gets detailed info for a single recovery point.
        """
        return self.session.request('recoveryPoints/rps/%s/details'
                % (recoveryPointId))

    def getRecoveryPointLockedKeys(self, recoveryPointId):
        """Gets a list of encryption keys used by a recovery
        point that are locked and require a passphrase in order to
        mount.
        """
        return self.session.request('recoveryPoints/rps/%s/lockedkeys'
                % (recoveryPointId))

    def getRecoveryPointSummary(self, recoveryPointId):
        """Gets detailed info for a single recovery point.
        """
        return self.session.request('recoveryPoints/rps/%s/summary'
                % (recoveryPointId))

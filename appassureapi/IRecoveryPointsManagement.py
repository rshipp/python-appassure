"""AppAssure 5 Core API
   IRecoveryPointsManagement
"""

from appassureapi import AppAssureAPI

class IRecoveryPointsManagement(AppAssureAPI):
    """Full documentation online at
       http://docs.appassure.com/display/AA50D/IRecoveryPointsManagement
    """

    def DeleteRecoveryPointsForAgent(self, agentId):
        """Summary: Deletes all recovery points for specified agent.
           URI: recoveryPoints/agents/{agentId}
           HTTP Method: DELETE
        """
        return self.session.request('recoveryPoints/agents/%s' 
                % (agentId), 'DELETE')

    def GetAllRecoveryPoints(self, agentId):
        """Summary: Gets the summary information for all recovery 
            points associated with the specified agent. Note that this 
            list can potentially be very large.
           URI: recoveryPoints/agents/{agentId}/all
           HTTP Method: GET
        """
        return self.session.request('recoveryPoints/agents/%s/all' 
                % (agentId))

    def StartCheckAgentRecoveryPoints(self, agentId, fixErrors):
        """Summary: Starts a task that performs integrity check of all 
            agent's recovery points and tries to fix errors being found
           URI: recoveryPoints/agents/{agentId}/integritycheck/fix?fixErrors={fixErrors}
           HTTP Method: GET
        """
        return self.session.request('recoveryPoints/agents/%s/integritycheck/fix?fixErrors=%s' 
                % (agentId, fixErrors))

    def GetRecoveryPointsByPage(self, agentId, page):
        """Summary: Gets summary info for recovery points for a given 
            agent ID, such that the results are paged for easy viewing 
            in a paged grid.
           URI: recoveryPoints/agents/{agentId}/paged?max={max}&page={page}
           HTTP Method: GET
        """
        return self.session.request('recoveryPoints/agents/%s/paged?max=%s&page=%s' 
                % (agentId, page))

    def GetRecoveryPoints(self, agentId):
        """Summary: Gets the summary information for the recovery 
            points associated with a specified agent that fall outside 
            of a last modified date/time range. You also specify a 
            maximum number of recovery points to return with the 
            specified range. {olderThan}&newerThan={newerThan}
           URI: recoveryPoints/agents/{agentId}/where?max={max}&olderThan=
           HTTP Method: GET
        """
        return self.session.request('recoveryPoints/agents/%s/where?max=%s&olderThan=' 
                % (agentId))

    def MergeAgentRecoveryPoints(self, data, sourceAgentId):
        """Summary: Merges the recovery points of the agent ID 
            identified by the URI into another agent ID specified in the 
            request.
           URI: recoveryPoints/agents/{sourceAgentId}
           HTTP Method: POST
        """
        return self.session.request('recoveryPoints/agents/%s' 
                % (sourceAgentId), 'POST', 
                    self.getXML(data, 'mergeRecoveryPointsRequest'))

    def GetAgentsRecoveryPointsInfo(self):
        """Summary: Gets a list of all agents with recovery points.
           URI: recoveryPoints/agents/all
           HTTP Method: GET
        """
        return self.session.request('recoveryPoints/agents/all')

    def GetVolumeImageDetails(self, imageId):
        """Summary: 'Gets information for a single volume image 
            specified by unique identifier.
           URI: recoveryPoints/images/{imageId}/
           HTTP Method: GET
        """
        return self.session.request('recoveryPoints/images/%s/' 
                % (imageId))

    def GetImageRawData(self):
        """Summary: Gets a stream of data consisting of the data in 
            the image at the specified offset and length. Useful only 
            for diagnostic purposes. 
            {blockOffset}&blockLength={blockLength}
           URI: recoveryPoints/images/rawdata/{imageId}.rawdata?blockOffset=
           HTTP Method: GET
        """
        return self.session.request('recoveryPoints/images/rawdata/%s.rawdata?blockOffset=' 
                % ())

    def GetImageRawKeys(self, imageId.rawkeys):
        """Summary: Gets a stream of offset/key pairs, containing the 
            block offsets in the image and the DVM keys of the record at 
            each block offset. Useful only for diagnostic purposes.
           URI: recoveryPoints/images/rawkeys/{imageId}.rawkeys
           HTTP Method: GET
        """
        return self.session.request('recoveryPoints/images/rawkeys/%s.rawkeys' 
                % (imageId.rawkeys))

    def GetImageRawKeysText(self, imageId.textkeys):
        """Summary: Gets a stream of offset/key pairs, containing the 
            block offsets in the image and the DVM keys of the record at 
            each block offset. Useful only for diagnostic purposes.
           URI: recoveryPoints/images/rawkeys/{imageId}.textkeys
           HTTP Method: GET
        """
        return self.session.request('recoveryPoints/images/rawkeys/%s.textkeys' 
                % (imageId.textkeys))

    def GetMostRecentRecoveryPoints(self, data):
        """Summary: Gets summary info for the most recent recovery 
            point of every agent specified in the request.
           URI: recoveryPoints/recent
           HTTP Method: PUT
        """
        return self.session.request('recoveryPoints/recent', 'PUT', 
                    self.getXML(data, 'getMostRecentRecoveryPoints'))

    def DeleteRecoveryPointsRange(self, data):
        """Summary: Deletes all recovery points in a specified time 
            period for the specified agent.
           URI: recoveryPoints/rps/deleteRecoveryPointsRange
           HTTP Method: POST
        """
        return self.session.request('recoveryPoints/rps/deleteRecoveryPointsRange', 'POST', 
                    self.getXML(data, 'adHocDeleteRecoveryPointsRequest'))

    def DeleteRecoveryPointsChain(self, recoveryPointId):
        """Summary: Deletes all volume image chains that contain 
            volume images for a given recovery point.
           URI: recoveryPoints/rps/{recoveryPointId}
           HTTP Method: DELETE
        """
        return self.session.request('recoveryPoints/rps/%s' 
                % (recoveryPointId), 'DELETE')

    def GetRecoveryPointDetails(self, recoveryPointId):
        """Summary: Gets detailed info for a single recovery point.
           URI: recoveryPoints/rps/{recoveryPointId}/details
           HTTP Method: GET
        """
        return self.session.request('recoveryPoints/rps/%s/details' 
                % (recoveryPointId))

    def GetRecoveryPointLockedKeys(self, recoveryPointId):
        """Summary: Gets a list of encryption keys used by a recovery 
            point that are locked and require a passphrase in order to 
            mount.
           URI: recoveryPoints/rps/{recoveryPointId}/lockedkeys
           HTTP Method: GET
        """
        return self.session.request('recoveryPoints/rps/%s/lockedkeys' 
                % (recoveryPointId))

    def GetRecoveryPointSummary(self, recoveryPointId):
        """Summary: Gets detailed info for a single recovery point.
           URI: recoveryPoints/rps/{recoveryPointId}/summary
           HTTP Method: GET
        """
        return self.session.request('recoveryPoints/rps/%s/summary' 
                % (recoveryPointId))


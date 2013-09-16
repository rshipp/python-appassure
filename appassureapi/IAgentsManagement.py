"""AppAssure 5 Core API
   IAgentsManagement
"""

from appassureapi import AppAssureAPI

class IAgentsManagement(AppAssureAPI):
    """Full documentation online at
       http://docs.appassure.com/display/AA50D/IAgentsManagement
    """

    def GetAgents(self):
        """Summary: Gets a list of all agents known to the core.
           URI: agents/
           HTTP Method: GET
        """
        return self.session.request('agents/')

    def GetCachedAgentMetadataById(self, agentId):
        """Summary: Gets cached metadata for an agent protected by 
            Replay.
           URI: agents/{agentId}/cachedmetadata
           HTTP Method: GET
        """
        return self.session.request('agents/%s/cachedmetadata' 
                % (agentId))

    def GetCachedAgentSummaryMetadataById(self, agentId):
        """Summary: Gets cached summary metadata for an agent 
            protected by Replay.
           URI: agents/{agentId}/cachedmetadata/summary
           HTTP Method: GET
        """
        return self.session.request('agents/%s/cachedmetadata/summary' 
                % (agentId))

    def ChangeDisplayName(self, agentId, newDisplayName):
        """Summary: Changes the display name used by the GUI for a 
            given Agent.
           URI: agents/{agentId}/changeDisplayName/{newDisplayName}
           HTTP Method: POST
        """
        return self.session.request('agents/%s/changeDisplayName/%s' 
                % (agentId, newDisplayName), 'POST')

    def ChangeHostName(self, agentId, newHostName):
        """Summary: Changes the host name used in connecting to a 
            given Agent.
           URI: agents/{agentId}/changeHostName/{newHostName}
           HTTP Method: POST
        """
        return self.session.request('agents/%s/changeHostName/%s' 
                % (agentId, newHostName), 'POST')

    def SetReplicatedAgentRepository(self, agentId, repositoryId):
        """Summary: Assigns a repository to an agent which was added 
            to replication.
           URI: agents/{agentId}/changeRepository/{repositoryId}
           HTTP Method: POST
        """
        return self.session.request('agents/%s/changeRepository/%s' 
                % (agentId, repositoryId), 'POST')

    def DeleteAgent(self, data, agentId):
        """Summary: Deletes an agent from the core, optionally deletes 
            the agent's recovery points and disables the agent's volumes 
            as well.
           URI: agents/{agentId}/delete
           HTTP Method: POST
        """
        return self.session.request('agents/%s/delete' 
                % (agentId), 'POST', 
                    self.getXML(data, 'deleteAgentRequest'))

    def ChangeAgentDescriptor(self, data, agentId):
        """Summary: Changes the descriptor used for an existing agent, 
            so the core will use a new caller-specified URI and 
            credentials.
           URI: agents/{agentId}/descriptor
           HTTP Method: POST
        """
        return self.session.request('agents/%s/descriptor' 
                % (agentId), 'POST', 
                    self.getXML(data, 'agentDescriptor'))

    def GetAgentDetails(self, agentId):
        """Summary: Gets all information required to display the Agent 
            Details page in the GUI.
           URI: agents/{agentId}/details
           HTTP Method: GET
        """
        return self.session.request('agents/%s/details' 
                % (agentId))

    def GetAgentInfo(self, agentId):
        """Summary: Gets the information about an agent protected by 
            Replay.
           URI: agents/{agentId}/info
           HTTP Method: GET
        """
        return self.session.request('agents/%s/info' 
                % (agentId))

    def GetAgentMetadataById(self, agentId):
        """Summary: Gets the latest metadata for an agent protected by 
            Replay.
           URI: agents/{agentId}/metadata
           HTTP Method: GET
        """
        return self.session.request('agents/%s/metadata' 
                % (agentId))

    def SetAgentMetadataCredentials(self, data, agentId):
        """Summary: Sets credentials which used for metadata retrival 
            for agent with specified Id
           URI: agents/{agentId}/metadata/credentials
           HTTP Method: POST
        """
        return self.session.request('agents/%s/metadata/credentials' 
                % (agentId), 'POST', 
                    self.getXML(data, 'credentialsDescriptor'))

    def GetAgentMetadataCredentials(self, agentId):
        """Summary: Gets credentials which used for metadata retrival 
            for agent with specified Id
           URI: agents/{agentId}/metadata/credentials
           HTTP Method: GET
        """
        return self.session.request('agents/%s/metadata/credentials' 
                % (agentId))

    def ForceAgentMetadataRefresh(self, agentId):
        """Summary: Forces metadata refresh for agent with specified Id
           URI: agents/{agentId}/metadata/refresh
           HTTP Method: POST
        """
        return self.session.request('agents/%s/metadata/refresh' 
                % (agentId), 'POST')

    def GetAgentSummaryMetadataById(self, agentId):
        """Summary: Gets latest summary metadata for an agent 
            protected by Core.
           URI: agents/{agentId}/metadata/summary
           HTTP Method: GET
        """
        return self.session.request('agents/%s/metadata/summary' 
                % (agentId))

    def VerifyCredentials(self, data, agentId):
        """Summary: Verifys that given credentials for the agent with 
            given Id are valid for retriving Exchange and SQL Server 
            metadata
           URI: agents/{agentId}/metadata/validator
           HTTP Method: POST
        """
        return self.session.request('agents/%s/metadata/validator' 
                % (agentId), 'POST', 
                    self.getXML(data, 'credentialsDescriptor'))

    def ChangePort(self, data, agentId):
        """Summary: Changes port used in connecting to a given Agent.
           URI: agents/{agentId}/port
           HTTP Method: POST
        """
        return self.session.request('agents/%s/port' 
                % (agentId), 'POST', 
                    self.getXML(data, 'agentPortChangeRequest'))

    def GetAgentSummaryInfo(self, agentId):
        """Summary: Gets summary agent information including summary 
            metadata, recent associated alerts and recent recovery 
            points.
           URI: agents/{agentId}/summaryInfo
           HTTP Method: GET
        """
        return self.session.request('agents/%s/summaryInfo' 
                % (agentId))

    def GetWriters(self, agentId):
        """Summary: Gets detailed information about VSS writers 
            installed on the agent.
           URI: agents/{agentId}/writers
           HTTP Method: GET
        """
        return self.session.request('agents/%s/writers' 
                % (agentId))

    def VerifyConnect(self, data):
        """Summary: Trying to connect to agent and return its Id.
           URI: agents/connect
           HTTP Method: POST
        """
        return self.session.request('agents/connect', 'POST', 
                    self.getXML(data, 'agentDescriptor'))

    def DeleteAgents(self, data):
        """Summary: Deletes agents from the core, optionally deletes 
            the agent's recovery points and disables the agent's volumes 
            as well.
           URI: agents/delete
           HTTP Method: POST
        """
        return self.session.request('agents/delete', 'POST', 
                    self.getXML(data, 'deleteAgentsRequest'))

    def GetAgentInfoSummaries(self):
        """             Summary:
           URI: agents/infosummaries
           HTTP Method: GET
        """
        return self.session.request('agents/infosummaries')

    def AddAgent(self, data):
        """Summary: Adds an agent that isn't currently protected, 
            pairs with the agent and writes it's protection 
            configuration.
           URI: agents/new
           HTTP Method: POST
        """
        return self.session.request('agents/new', 'POST', 
                    self.getXML(data, 'addAgentRequest'))

    def AddAgents(self, data):
        """             Summary:
           URI: agents/newagents
           HTTP Method: POST
        """
        return self.session.request('agents/newagents', 'POST', 
                    self.getXML(data, 'addAgentsRequest'))

    def RepairPairing(self, data):
        """Summary: Attempts to re-establish pairing with an agent 
            already protected by the core, possibly using new 
            credentials.
           URI: agents/pairing/repair
           HTTP Method: POST
        """
        return self.session.request('agents/pairing/repair', 'POST', 
                    self.getXML(data, 'agentDescriptor'))

    def RepairOrphanedPairing(self, data):
        """Summary: Attempts to re-establish pairing with an agent 
            already protected by the core using existing credentials.
           URI: agents/pairing/repairOrphan
           HTTP Method: POST
        """
        return self.session.request('agents/pairing/repairOrphan', 'POST', 
                    self.getXML(data, 'agentDescriptor'))

    def GetProtectedAgents(self):
        """Summary: Gets a list of protected agents known to the core.
           URI: agents/protected
           HTTP Method: GET
        """
        return self.session.request('agents/protected')

    def GetAgentVolumeGroupsAvailableForProtection(self, data):
        """Summary: Connects to an agent specified in the descriptor 
            (probably not currently protected by this core) and requests 
            the list of volumes which are available for protection, 
            grouped to reflect protection dependencies. It is possible 
            that an agent and a core are installed on the same machine 
            so a resulting list would not contain volumes which contain 
            core repository data or metadata directories. For regular 
            cases this list would be identical to a list of volumes 
            returned in metadata.
           URI: agents/query/availableGroups
           HTTP Method: PUT
        """
        return self.session.request('agents/query/availableGroups', 'PUT', 
                    self.getXML(data, 'agentDescriptor'))

    def GetAgentVolumesAvailableForProtection(self, data):
        """Summary: Connects to an agent specified in the descriptor 
            (probably not currently protected by this core) and requests 
            the list of volumes which are available for protection. It 
            is possible that an agent and a core are installed on the 
            same machine so a resulting list would not contain volumes 
            which contain core repository data or metadata directories. 
            For regular cases this list would be identical to a list of 
            volumes returned in metadata.
           URI: agents/query/availablevolumes
           HTTP Method: PUT
        """
        return self.session.request('agents/query/availablevolumes', 'PUT', 
                    self.getXML(data, 'agentDescriptor'))

    def CheckAgentPairing(self, data):
        """Summary: Connects to an agent specified in the descriptor 
            (probably not currently protected by this core) and checks 
            if the agent is paired to this core or any core at all.
           URI: agents/query/checkpairing
           HTTP Method: PUT
        """
        return self.session.request('agents/query/checkpairing', 'PUT', 
                    self.getXML(data, 'agentDescriptor'))

    def GetAgentMetadata(self, data):
        """Summary: Connects to an agent specified in the descriptor 
            (probably not currently protected by this core) and requests 
            the agent's metadata.
           URI: agents/query/metadata
           HTTP Method: PUT
        """
        return self.session.request('agents/query/metadata', 'PUT', 
                    self.getXML(data, 'agentDescriptor'))

    def GetPairingSettings(self, data):
        """Summary: Connects to an agent specified in the descriptor 
            (probably not currently protected by this core) and requests 
            the agent's pairing information.
           URI: agents/query/pairing
           HTTP Method: PUT
        """
        return self.session.request('agents/query/pairing', 'PUT', 
                    self.getXML(data, 'agentDescriptor'))

    def GetAgentSummaryMetadata(self, data):
        """Summary: Connects to an agent specified in the descriptor 
            (probably not currently protected by this core) and requests 
            the agent's summary metadata.
           URI: agents/query/summarymetadata
           HTTP Method: PUT
        """
        return self.session.request('agents/query/summarymetadata', 'PUT', 
                    self.getXML(data, 'agentDescriptor'))

    def GetRecoveryPointsOnlyAgents(self):
        """Summary: Gets a list of recovery points' only agents
           URI: agents/recoveryPointsOnly
           HTTP Method: GET
        """
        return self.session.request('agents/recoveryPointsOnly')

    def GetReplicatedAgents(self):
        """Summary: Gets a list of replicated agents known to the core.
           URI: agents/replicated
           HTTP Method: GET
        """
        return self.session.request('agents/replicated')


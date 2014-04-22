"""AppAssure 5 Core API"""

from appassure.api import AppAssureAPI

class IAgentsManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IAgentsManagement
    """

    def getAgents(self):
        """Gets a list of all agents known to the core."""
        return self.session.request('agents/')

    def getCachedAgentMetadataById(self, agentId):
        """Gets cached metadata for an agent protected by
        Replay.
        """
        return self.session.request('agents/%s/cachedmetadata'
                % (agentId))

    def getCachedAgentSummaryMetadataById(self, agentId):
        """Gets cached summary metadata for an agent
        protected by Replay.
        """
        return self.session.request('agents/%s/cachedmetadata/summary'
                % (agentId))

    def changeDisplayName(self, agentId, newDisplayName):
        """Changes the display name used by the GUI for a
        given Agent.
        """
        return self.session.request('agents/%s/changeDisplayName/%s'
                % (agentId, newDisplayName), 'POST')

    def changeHostName(self, agentId, newHostName):
        """Changes the host name used in connecting to a
        given Agent.
        """
        return self.session.request('agents/%s/changeHostName/%s'
                % (agentId, newHostName), 'POST')

    def setReplicatedAgentRepository(self, agentId, repositoryId):
        """Assigns a repository to an agent which was added
        to replication.
        """
        return self.session.request('agents/%s/changeRepository/%s'
                % (agentId, repositoryId), 'POST')

    def deleteAgent(self, data, agentId):
        """Deletes an agent from the core, optionally deletes
        the agent's recovery points and disables the agent's volumes
        as well.
        """
        return self.session.request('agents/%s/delete'
                % (agentId), 'POST',
                    self.getXML(data, 'deleteAgentRequest'))

    def changeAgentDescriptor(self, data, agentId):
        """Changes the descriptor used for an existing agent,
        so the core will use a new caller-specified URI and
        credentials.
        """
        return self.session.request('agents/%s/descriptor'
                % (agentId), 'POST',
                    self.getXML(data, 'agentDescriptor'))

    def getAgentDetails(self, agentId):
        """Gets all information required to display the Agent
        Details page in the GUI.
        """
        return self.session.request('agents/%s/details'
                % (agentId))

    def getAgentInfo(self, agentId):
        """Gets the information about an agent protected by
        Replay.
        """
        return self.session.request('agents/%s/info'
                % (agentId))

    def getAgentMetadataById(self, agentId):
        """Gets the latest metadata for an agent protected by
        Replay.
        """
        return self.session.request('agents/%s/metadata'
                % (agentId))

    def setAgentMetadataCredentials(self, data, agentId):
        """Sets credentials which used for metadata retrival
        for agent with specified Id
        """
        return self.session.request('agents/%s/metadata/credentials'
                % (agentId), 'POST',
                    self.getXML(data, 'credentialsDescriptor'))

    def getAgentMetadataCredentials(self, agentId):
        """Gets credentials which used for metadata retrival
        for agent with specified Id
        """
        return self.session.request('agents/%s/metadata/credentials'
                % (agentId))

    def forceAgentMetadataRefresh(self, agentId):
        """Forces metadata refresh for agent with specified Id
        """
        return self.session.request('agents/%s/metadata/refresh'
                % (agentId), 'POST')

    def getAgentSummaryMetadataById(self, agentId):
        """Gets latest summary metadata for an agent
        protected by Core.
        """
        return self.session.request('agents/%s/metadata/summary'
                % (agentId))

    def verifyCredentials(self, data, agentId):
        """Verifys that given credentials for the agent with
        given Id are valid for retriving Exchange and SQL Server
        metadata
        """
        return self.session.request('agents/%s/metadata/validator'
                % (agentId), 'POST',
                    self.getXML(data, 'credentialsDescriptor'))

    def changePort(self, data, agentId):
        """Changes port used in connecting to a given Agent.
        """
        return self.session.request('agents/%s/port'
                % (agentId), 'POST',
                    self.getXML(data, 'agentPortChangeRequest'))

    def getAgentSummaryInfo(self, agentId):
        """Gets summary agent information including summary
        metadata, recent associated alerts and recent recovery
        points.
        """
        return self.session.request('agents/%s/summaryInfo'
                % (agentId))

    def getWriters(self, agentId):
        """Gets detailed information about VSS writers
        installed on the agent.
        """
        return self.session.request('agents/%s/writers'
                % (agentId))

    def verifyConnect(self, data):
        """Trying to connect to agent and return its Id.
        """
        return self.session.request('agents/connect', 'POST',
                    self.getXML(data, 'agentDescriptor'))

    def deleteAgents(self, data):
        """Deletes agents from the core, optionally deletes
        the agent's recovery points and disables the agent's volumes
        as well.
        """
        return self.session.request('agents/delete', 'POST',
                    self.getXML(data, 'deleteAgentsRequest'))

    def getAgentInfoSummaries(self):
        """ """
        return self.session.request('agents/infosummaries')

    def addAgent(self, data):
        """Adds an agent that isn't currently protected,
        pairs with the agent and writes it's protection
        configuration.
        """
        return self.session.request('agents/new', 'POST',
                    self.getXML(data, 'addAgentRequest'))

    def addAgents(self, data):
        """ """
        return self.session.request('agents/newagents', 'POST',
                    self.getXML(data, 'addAgentsRequest'))

    def repairPairing(self, data):
        """Attempts to re-establish pairing with an agent
        already protected by the core, possibly using new
        credentials.
        """
        return self.session.request('agents/pairing/repair', 'POST',
                    self.getXML(data, 'agentDescriptor'))

    def repairOrphanedPairing(self, data):
        """Attempts to re-establish pairing with an agent
        already protected by the core using existing credentials.
        """
        return self.session.request('agents/pairing/repairOrphan', 'POST',
                    self.getXML(data, 'agentDescriptor'))

    def getProtectedAgents(self):
        """Gets a list of protected agents known to the core.
        """
        return self.session.request('agents/protected')

    def getAgentVolumeGroupsAvailableForProtection(self, data):
        """Connects to an agent specified in the descriptor
        (probably not currently protected by this core) and requests
        the list of volumes which are available for protection,
        grouped to reflect protection dependencies. It is possible
        that an agent and a core are installed on the same machine
        so a resulting list would not contain volumes which contain
        core repository data or metadata directories. For regular
        cases this list would be identical to a list of volumes
        returned in metadata.
        """
        return self.session.request('agents/query/availableGroups', 'PUT',
                    self.getXML(data, 'agentDescriptor'))

    def getAgentVolumesAvailableForProtection(self, data):
        """Connects to an agent specified in the descriptor
        (probably not currently protected by this core) and requests
        the list of volumes which are available for protection. It
        is possible that an agent and a core are installed on the
        same machine so a resulting list would not contain volumes
        which contain core repository data or metadata directories.
        For regular cases this list would be identical to a list of
        volumes returned in metadata.
        """
        return self.session.request('agents/query/availablevolumes', 'PUT',
                    self.getXML(data, 'agentDescriptor'))

    def checkAgentPairing(self, data):
        """Connects to an agent specified in the descriptor
        (probably not currently protected by this core) and checks
        if the agent is paired to this core or any core at all.
        """
        return self.session.request('agents/query/checkpairing', 'PUT',
                    self.getXML(data, 'agentDescriptor'))

    def getAgentMetadata(self, data):
        """Connects to an agent specified in the descriptor
        (probably not currently protected by this core) and requests
        the agent's metadata.
        """
        return self.session.request('agents/query/metadata', 'PUT',
                    self.getXML(data, 'agentDescriptor'))

    def getPairingSettings(self, data):
        """Connects to an agent specified in the descriptor
        (probably not currently protected by this core) and requests
        the agent's pairing information.
        """
        return self.session.request('agents/query/pairing', 'PUT',
                    self.getXML(data, 'agentDescriptor'))

    def getAgentSummaryMetadata(self, data):
        """Connects to an agent specified in the descriptor
        (probably not currently protected by this core) and requests
        the agent's summary metadata.
        """
        return self.session.request('agents/query/summarymetadata', 'PUT',
                    self.getXML(data, 'agentDescriptor'))

    def getRecoveryPointsOnlyAgents(self):
        """Gets a list of recovery points' only agents
        """
        return self.session.request('agents/recoveryPointsOnly')

    def getReplicatedAgents(self):
        """Gets a list of replicated agents known to the core.
        """
        return self.session.request('agents/replicated')

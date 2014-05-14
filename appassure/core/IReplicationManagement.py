"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IReplicationManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IReplicationManagement
    """

    def setAgentReplicationSettings(self, data, agentId):
        """Set replication settings into an agent with given ID."""
        return self.session.request('replication/agents/%s'
                % (agentId), 'PUT',
                    self.getXML(data, 'agentReplicationSettings'))

    def getAgentReplicationSettings(self, agentId):
        """Get replication settings for agent with given ID."""
        return self.session.request('replication/agents/%s'
                % (agentId))

    def getReplicationConfiguration(self):
        """Gets replication configuration."""
        return self.session.request('replication/config')

    def setReplicationConfiguration(self, data):
        """Sets replication configuration."""
        return self.session.request('replication/config', 'PUT',
                    self.getXML(data, 'replicationServiceConfig'))

    def getRemoteCores(self, forceRefresh):
        """Gets a list of all of the remote cores this core knows
        about, both master and slave.
        """
        return self.session.request('replication/cores/?forceRefresh=%s'
                % (forceRefresh))

    def switchReplicatedAgentToFailover(self, coreId, agentId):
        """Converts failover agent to replicated agent.
        failback?ignoreRunningReplicationJobs={ignoreReplication}.
        """
        return self.session.request('replication/cores/%s/agents/%s/'
                % (coreId, agentId), 'POST')

    def switchFailoverAgentToReplicated(self, coreId, agentId):
        """Converts replicated agent to failover."""
        return self.session.request('replication/cores/%s/agents/%s/failover'
                % (coreId, agentId), 'POST')

    def getRemoteAgentsRecoveryPoints(self, coreId, agentid):
        """Gets the replicated recovery points on a remote slave
        core for the specific agent. This won't work with a master core.
        """
        return self.session.request('replication/cores/%s/agents/%s/recoveryPoints'
                % (coreId, agentid))

    def getCountRemoteAgentsRecoveryPoints(self, coreId, agentid):
        """Gets count of replicated recovery points on a remote
        slave core for the specific agent. This won't work with a master
        core.
        """
        return self.session.request('replication/cores/%s/agents/%s/recoveryPointsCount'
                % (coreId, agentid))

    def getRemoteSlaveRecoveryPoint(self, coreId, agentId, recoveryPointId):
        """Gets the details for a replicated recovery point on a
        remote slave core. This won't work with a master core.
        """
        return self.session.request('replication/cores/%s/agents/%s/rps/%s'
                % (coreId, agentId, recoveryPointId))

    def selectRangeRemoteAgentsRecoveryPoints(self, coreId, agentid, skipCount):
        """Gets the range of replicated recovery points on a
        remote slave core for the specific agent. This won't work with a
        master core. maxCount/{maxCount}/recoveryPoints.
        """
        return self.session.request('replication/cores/%s/agents/%s/skipCount/%s/'
                % (coreId, agentid, skipCount))

    def addAgentsByDemand(self, data, coreId):
        """Add agents to existing pairing by demand."""
        return self.session.request('replication/cores/%s/agents/demand'
                % (coreId), 'POST',
                    self.getXML(data, 'addAgentsDemand'))

    def addAgentsByRequest(self, data, coreId):
        """Add agents to existing pairing by request."""
        return self.session.request('replication/cores/%s/agents/request'
                % (coreId), 'POST',
                    self.getXML(data, 'addAgentsRequest'))

    def getReplicatedAgentsRecoveryPointsInfo(self, coreId):
        """Gets the list of agents which have recovery points on
        a remote slave core.
        """
        return self.session.request('replication/cores/%s/agents/rpsinfo'
                % (coreId))

    def deletePairing(self, coreId):
        """Delete pairing between master and slave cores.
        {deleteRecoveryPoints}.
        """
        return self.session.request('replication/cores/%s/pairing?deleteRecoveryPoints='
                % (coreId))

    def getCoreIdByUrl(self, hostUri):
        """Tests connection to a remote core. Returns CoreId.
        Using Anonymous authentication.
        """
        return self.session.request('replication/cores/%s'
                % (hostUri), 'PUT')

    def getCoreIdByDescriptor(self, data):
        """Tests a core descriptor to validate the ability to
        connect to it. Returns CoreId. Using NTLM authentication.
        """
        return self.session.request('replication/cores/descriptor', 'PUT',
                    self.getXML(data, 'remoteCoreDescriptor'))

    def demandPairing(self, data):
        """Instructs this core to send a replication demand to a
        remote core. This operation will require admin credentials on
        the remote core, but if successful will take effect right away.
        Returns slave core Id.
        """
        return self.session.request('replication/cores/pairing/demand', 'POST',
                    self.getXML(data, 'remoteCoreReplicationPairingDemand'))

    def requestPairing(self, data):
        """Instructs this core to send a replication request to a
        remote core. Replication will start once the remote core
        approves the request. Returns slave core Id.
        """
        return self.session.request('replication/cores/pairing/request', 'POST',
                    self.getXML(data, 'remoteCoreReplicationPairingRequest'))

    def verifyAddAgentsByDemandForExistingCore(self, data, coreId):
        """Verifies whether agents can be safely replicated by
        demand.
        """
        return self.session.request('replication/cores/slave/%s/agents/demand/verify'
                % (coreId), 'POST',
                    self.getXML(data, 'addAgentsVerificationByDemand'))

    def verifyAddAgentsByRequestForExistingCore(self, data, coreId):
        """Verifies whether agents can be safely replicated by
        request.
        """
        return self.session.request('replication/cores/slave/%s/agents/request/verify'
                % (coreId), 'POST',
                    self.getXML(data, 'addAgentsVerificationByRequest'))

    def verifyAddAgentsByDemand(self, data):
        """Verifies whether agents can be safely replicated by
        demand.
        """
        return self.session.request('replication/cores/slave/agents/demand/verify', 'POST',
                    self.getXML(data, 'addAgentsVerificationByDemand'))

    def verifyAddAgentsByRequest(self, data):
        """Verifies whether agents can be safely replicated by
        request.
        """
        return self.session.request('replication/cores/slave/agents/request/verify', 'POST',
                    self.getXML(data, 'addAgentsVerificationByRequest'))

    def getRemoteMasterCoresForDemand(self, data):
        """Getting remote masers cores info for current slave
        core.
        """
        return self.session.request('replication/cores/slave/masters', 'PUT',
                    self.getXML(data, 'remoteCoreDescriptor'))

    def getRemoteCoreRepositories(self, data):
        """Gets the repositories on a remote core. Admin
        credentials on the remote core are required.
        """
        return self.session.request('replication/cores/slave/repositories', 'PUT',
                    self.getXML(data, 'remoteCoreDescriptor'))

    def getAgentRepositoryRelationships(self, slaveCoreId):
        """Gets the repositories on a remote core for agents."""
        return self.session.request('replication/cores/slaves/%s/agentRepositoryRelationships'
                % (slaveCoreId))

    def getRemoteCoreRepositoriesForDemand(self, slaveCoreId):
        """Gets the repositories on a remote core for. Uses
        certificate authentication and works only for demanded core.
        """
        return self.session.request('replication/cores/slaves/%s/pairingdemand/repositories'
                % (slaveCoreId), 'PUT')

    def updateSlaveCoreSettings(self, data, slaveCoreId):
        """Sets remote slave core configuration. This work with a
        master core side only.
        """
        return self.session.request('replication/cores/slaves/%s/settings'
                % (slaveCoreId), 'PUT',
                    self.getXML(data, 'updateCoreSettingsRequest'))

    def setRemoteSlaveCoreReplicationPolicy(self, data, slaveCoreId):
        """Sets remote slave core replication policy. This work
        with a master core side only.
        """
        return self.session.request('replication/cores/slaves/%s/settings/policy'
                % (slaveCoreId), 'PUT',
                    self.getXML(data, 'replicationPolicy'))

    def getRemoteSlaveCoreReplicationPolicy(self, slaveCoreId):
        """Gets remote slave core replication policy. This work
        with a master core side only.
        """
        return self.session.request('replication/cores/slaves/%s/settings/policy'
                % (slaveCoreId))

    def verifyCorePairingAbilityByDemand(self, data):
        """Tests a core descriptor to validate the ability to
        create pairing to remote core. Returns CoreId. Using NTLM
        authentication.
        """
        return self.session.request('replication/cores/verify/demand', 'PUT',
                    self.getXML(data, 'remoteCoreDescriptor'))

    def verifyCorePairingAbilityByRequest(self, hostUri):
        """Tests a core descriptor to validate the ability to
        create pairing to remote core. Returns CoreId. Using anonymous
        authentication.
        """
        return self.session.request('replication/cores/verify/request/%s'
                % (hostUri), 'PUT')

    def forceReplication(self, data):
        """Force replication for agents."""
        return self.session.request('replication/force', 'PUT',
                    self.getXML(data, 'forceReplicationRequest'))

    def deleteAgentFromMaster(self, coreId, agentId):
        """Delete agent from replication relationship from
        slave's side only. Actual replicated and protected agent on
        master and slave cores stay available.
        ?deleteRecoveryPoints={deleteRecoveryPoints}.
        """
        return self.session.request('replication/masters/%s/replicatedagents/%s/'
                % (coreId, agentId))

    def deleteMasterCore(self, deleteRecoveryPoints):
        """Delete remote master core from replication."""
        return self.session.request('replication/masters/%s?deleteRecoveryPoints=%s'
                % (deleteRecoveryPoints))

    def setAgentReplicationPauseConfigurationForMasterCores(self, data, masterCoreId, agentId):
        """Pauses replication for agent."""
        return self.session.request('replication/masters/%s/agents/%s/pauseConfiguration'
                % (masterCoreId, agentId), 'POST',
                    self.getXML(data, 'replicationPauseConfiguration'))

    def requestForceReplication(self, data):
        """Request force replication."""
        return self.session.request('replication/requestForceReplication', 'PUT',
                    self.getXML(data, 'forceReplicationRequest'))

    def ignorePairingRequest(self, requestId):
        """Deletes a pending replication request without
        responding to it.
        """
        return self.session.request('replication/requests/%s'
                % (requestId))

    def respondToPairingRequest(self, data, requestId):
        """Responds to a pending replication requests."""
        return self.session.request('replication/requests/pairing/%s'
                % (requestId), 'POST',
                    self.getXML(data, 'pendingReplicationPairingResponse'))

    def respondToAddAgentsByRequest(self, data, requestId):
        """Responds to a pending agents from replication requests."""
        return self.session.request('replication/requests/pairing/%s/agents'
                % (requestId), 'POST',
                    self.getXML(data, 'pendingReplicationAgents'))

    def getPendingPairingRequest(self, requestId):
        """Gets a the pending request for a specific request ID."""
        return self.session.request('replication/requests/pairing/pending/%s'
                % (requestId))

    def getPendingPairingRequests(self):
        """Gets a list of all pending replication pairing
        requests received by this core from remote master cores.
        """
        return self.session.request('replication/requests/pending')

    def deleteSlaveCore(self, coreId):
        """Delete remote slave core from replication."""
        return self.session.request('replication/slaves/%s'
                % (coreId))

    def deleteAgentFromSlave(self, coreId, agentId):
        """Delete agent from replication relationship from
        master's side only. Actual replicated and protected agent on
        master and slave cores stay available.
        """
        return self.session.request('replication/slaves/%s/replicatedagents/%s'
                % (coreId, agentId))

    def setAgentReplicationPauseConfiguration(self, data, slaveCoreId, agentId):
        """Pauses replication for agent."""
        return self.session.request('replication/slaves/%s/agents/%s/pauseConfiguration'
                % (slaveCoreId, agentId), 'POST',
                    self.getXML(data, 'replicationPauseConfiguration'))

    def setAgentReplicationPauseConfigurationForSlaveCores(self, data, agentId):
        """Pauses replication for agent."""
        return self.session.request('replication/slaves/agents/%s/pauseConfiguration'
                % (agentId), 'POST',
                    self.getXML(data, 'replicationPauseConfiguration'))

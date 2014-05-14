"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IReplicationCommunication(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IReplicationCommunication
    """

    def getConsumedSeedDrives(self, agentId):
        """Gets identifiers of seed drives consumed on the Core
        for specified agent.
        """
        return self.session.request('replicationcomms/consumedSeedDrives/%s'
                % (agentId))

    def getReplicatedAgents(self):
        """Gets the list of agents the caller is replicating to
        this slave core. A pairing must be in place, and this request
        must be authenticated by the master core's client certificate.
        """
        return self.session.request('replicationcomms/slave/agents')

    def getReplicatedAgentsStorageUsage(self):
        """Gets a summary of storage usage of the replicated
        agents.
        """
        return self.session.request('replicationcomms/slave/agents')

    def getRepositoryFreeSpaceForAgent(self, agentId):
        """Get free space for agent's remote repository."""
        return self.session.request('replicationcomms/slave/agents/%s'
                % (agentId))

    def deleteAgent(self, agentId):
        """Deletes a replicated agent from the slave core,
        including all of its recovery points.
        """
        return self.session.request('replicationcomms/slave/agents/%s'
                % (agentId))

    def startMetadataUpdate(self, data, agentId):
        """Starts metadata update for specified agent."""
        return self.session.request('replicationcomms/slave/agents/%s/metadataUpdate'
                % (agentId), 'POST',
                    self.getXML(data, 'startMetadataUpdateRequest'))

    def cancelRemoteMetadataUpdate(self, agentId):
        """Cancels metadata update phase of replication job for
        replicated agent.
        """
        return self.session.request('replicationcomms/slave/agents/%s/metadataUpdate'
                % (agentId))

    def getMetadataUpdateProgress(self, agentId):
        """Gets status of the metadata update job initiated from
        master core.
        """
        return self.session.request('replicationcomms/slave/agents/%s/metadataUpdate/status'
                % (agentId))

    def startMetadataUpdateJob(self, data, agentId):
        """Starts metadata update job for specified agent."""
        return self.session.request('replicationcomms/slave/agents/%s/metadataUpdateJob'
                % (agentId), 'POST',
                    self.getXML(data, 'startMetadataUpdateRequest'))

    def getBasicReplicatedVolumeImagesInfo(self, agentId):
        """Gets the details for all recovery points replicated
        for the given agent.
        """
        return self.session.request('replicationcomms/slave/agents/%s/replicatedVolumeImages'
                % (agentId))

    def verifyReplicationAbility(self, agentId):
        """Verifies replication ability."""
        return self.session.request('replicationcomms/slave/agents/%s/replication/verifyStart'
                % (agentId))

    def startRollup(self, data, agentId):
        """Starts rollup for specified slave agent for specified
        granularity cells (time intervals).
        """
        return self.session.request('replicationcomms/slave/agents/%s/rollup'
                % (agentId), 'POST',
                    self.getXML(data, 'startRemoteRollupRequest'))

    def cancelRemoteRollup(self, agentId):
        """Cancels rollup phase of replication job for replicated
        agent.
        """
        return self.session.request('replicationcomms/slave/agents/%s/rollup'
                % (agentId))

    def getRollupProgress(self, agentId):
        """Gets status of the rollup job initiated from master
        core.
        """
        return self.session.request('replicationcomms/slave/agents/%s/rollup/progress'
                % (agentId))

    def startRollupJob(self, data, agentId):
        """Starts rollup job for specified slave agent for
        specified granularity cells (time intervals).
        """
        return self.session.request('replicationcomms/slave/agents/%s/rollupJob'
                % (agentId), 'POST',
                    self.getXML(data, 'startRemoteRollupRequest'))

    def getAgentRecoveryPoints(self, agentId):
        """Gets the recovery points replicated for the given
        agent.
        """
        return self.session.request('replicationcomms/slave/agents/%s/rps'
                % (agentId))

    def getAgentRecoveryPointDetails(self, agentId, recoveryPointId):
        """Gets the details for a single replicated recovery
        point.
        """
        return self.session.request('replicationcomms/slave/agents/%s/rps/%s'
                % (agentId, recoveryPointId))

    def getAgentRecoveryPointsCounts(self, agentId):
        """Gets count of the recovery points replicated for the
        given agent.
        """
        return self.session.request('replicationcomms/slave/agents/%s/rpsCount'
                % (agentId))

    def selectRangeAgentRecoveryPoints(self, agentId, skipCount):
        """Select range of the recovery points replicated for the
        given agent. {maxCount}/rps.
        """
        return self.session.request('replicationcomms/slave/agents/%s/skipCount/%s/maxCount/'
                % (agentId, skipCount))

    def updateReplicationStatus(self, data, agentId):
        """Set replication status on the slave core."""
        return self.session.request('replicationcomms/slave/agents/%s/status'
                % (agentId), 'PUT',
                    self.getXML(data, 'job'))

    def startTransferJob(self, agentId, jobId):
        """Starts remote mirrored transfer job on slave core."""
        return self.session.request('replicationcomms/slave/agents/%s/transferJob/%s'
                % (agentId, jobId), 'POST')

    def startVolumeImagesDeletionOld(self, data, agentId):
        """Starts deletion of volume images with specified
        identifiers for specified agent.
        """
        return self.session.request('replicationcomms/slave/agents/%s/volumeImagesDeletion'
                % (agentId), 'POST',
                    self.getXML(data, 'startRemoteVolumeImagesDeletionRequest'))

    def cancelRemoteVolumeImagesDeletion(self, agentId):
        """Cancels volume images deletion phase of replication
        job for replicated agent.
        """
        return self.session.request('replicationcomms/slave/agents/%s/volumeImagesDeletion'
                % (agentId))

    def getVolumeImagesDeletionProgress(self, agentId):
        """Gets status of the deletion job initiated from master
        core.
        """
        return self.session.request('replicationcomms/slave/agents/%s/volumeImagesDeletion/progress'
                % (agentId))

    def startVolumeImagesDeletionJobOld(self, data, agentId):
        """Starts deletion of volume images job with specified
        identifiers for specified agent.
        """
        return self.session.request('replicationcomms/slave/agents/%s/volumeImagesDeletionJob'
                % (agentId), 'POST',
                    self.getXML(data, 'startRemoteVolumeImagesDeletionRequest'))

    def startVolumeImagesDeletionJob(self, data, agentId):
        """Starts deletion of volume images job with specified
        identifiers for specified agent.
        """
        return self.session.request('replicationcomms/slave/agents/%s/volumeImagesDeletionJobNew'
                % (agentId), 'POST',
                    self.getXML(data, 'startRemoteVolumeImagesDeletionRequest'))

    def startVolumeImagesDeletion(self, data, agentId):
        """Starts deletion of volume images with specified
        identifiers for specified agent.
        """
        return self.session.request('replicationcomms/slave/agents/%s/volumeImagesDeletionNew'
                % (agentId), 'POST',
                    self.getXML(data, 'startRemoteVolumeImagesDeletionRequest'))

    def addAgentsByDemand(self, data):
        """Add agents by demand to a remote slave core."""
        return self.session.request('replicationcomms/slave/agents/demand', 'POST',
                    self.getXML(data, 'addAgentsDemand'))

    def startRemoteReplicationJob(self, data):
        """Starts remote mirrored replication job on slave core."""
        return self.session.request('replicationcomms/slave/agents/replicationJob/start', 'POST',
                    self.getXML(data, 'remoteReplicationJobRequest'))

    def syncRemoteReplicationJob(self, data):
        """Sync with remote mirrored replication job on slave
        core.
        """
        return self.session.request('replicationcomms/slave/agents/replicationJob/sync', 'POST',
                    self.getXML(data, 'remoteSyncReplicationJobRequest'))

    def addAgentsByRequest(self, data):
        """Add agents by request to a remote slave."""
        return self.session.request('replicationcomms/slave/agents/request', 'POST',
                    self.getXML(data, 'addAgentsRequest'))

    def getReplicatedAgentsRecoveryPointsInfo(self):
        """Gets the list of agents which have recovery points on
        a remote slave core.
        """
        return self.session.request('replicationcomms/slave/agents/rpsinfo')

    def getAgentRepositoryRelationships(self):
        """Gets the repositories for replicated agents."""
        return self.session.request('replicationcomms/slave/cores/agentRepositoryRelationships')

    def getRemoteMasterCoresForDemand(self):
        """Getting remote masers cores info for current slave
        core. Using NTLM authentication.
        """
        return self.session.request('replicationcomms/slave/cores/masters')

    def verifyAddAgentsByDemand(self, data):
        """Verifies whether agents can be safely replicated by
        demand.
        """
        return self.session.request('replicationcomms/slave/demand/agents/verify', 'POST',
                    self.getXML(data, 'addAgentsDemand'))

    def getExchangeVersions(self):
        """Gets versions of Exchange dlls, with present on remote
        slave core.
        """
        return self.session.request('replicationcomms/slave/exchange')

    def getFileInfoForExchangeDll(self, data, fileName):
        """Gets information for given Exchange DLL file."""
        return self.session.request('replicationcomms/slave/exchange/dllinfo/%s'
                % (fileName), 'POST',
                    self.getXML(data, 'ExchangeServerVersion xmlns="http://schemas.datacontract.org/2004/07/Replay.Common.Contracts.Metadata.Exchange"'))

    def startNewUploadSession(self, data):
        """Starts new file upload session."""
        return self.session.request('replicationcomms/slave/newsession/', 'POST',
                    self.getXML(data, 'fileReceiveRequest'))

    def demandPairing(self, data):
        """Demands the establishment of a pairing relationship
        with a remote core. Demands are only accepted if the caller
        performs NTLM authentication as a member of the administrators
        group. This method will reset connection for establish new
        secured connection.
        """
        return self.session.request('replicationcomms/slave/pairing/demand', 'POST',
                    self.getXML(data, 'replicationPairingDemand'))

    def requestPairing(self, data):
        """Sends a request to a remote slave for authorization to
        replicate one or more agents. The request is adjudicated by a
        human operator and will be approved or denied at a later date.
        This method will reset connection for establish new secured
        connection.
        """
        return self.session.request('replicationcomms/slave/pairing/request', 'POST',
                    self.getXML(data, 'replicationPairingRequest'))

    def getPairingStatus(self):
        """Gets the status of the pairing between the calling
        core and the remote slave core. The caller is identified by its
        SSL client certificate. This method is available to a remote
        core regardless of whether it was paired via a request or
        initiated the pairing itself.
        """
        return self.session.request('replicationcomms/slave/pairing/status')

    def syncPairingStatus(self, data):
        """Gets the status of the pairing between the calling
        core and the remote slave core. The caller is identified by its
        SSL client certificate. This method is available to a remote
        core regardless of whether it was paired via a request or
        initiated the pairing itself.
        """
        return self.session.request('replicationcomms/slave/pairing/sync', 'POST',
                    self.getXML(data, 'masterCorePairingStatus'))

    def deletePairing(self, deleteRecoveryPoints):
        """Removes replication relationship with Master Core on
        Slave's Core side. Actual replicated and protected agent on
        Master and Slave Cores stay available.
        """
        return self.session.request('replicationcomms/slave/pairing?deleteRecoveryPoints=%s'
                % (deleteRecoveryPoints))

    def verifyReplicationCorePairingAbility(self, data):
        """Verifies pairing ability. {useCredentials}."""
        return self.session.request('replicationcomms/slave/replication/verifyStart/?useCredentials=', 'POST',
                    self.getXML(data, 'remoteMasterSummaryCoreInfo'))

    def getRepositories(self):
        """Gets all repositories. With certificate authentication
        for already paired cores.
        """
        return self.session.request('replicationcomms/slave/repositories')

    def verifyAddAgentsByRequest(self, data):
        """Verifies whether agents can be safely replicated by
        request.
        """
        return self.session.request('replicationcomms/slave/request/agents/verify', 'POST',
                    self.getXML(data, 'addAgentsRequest'))

    def negotiateMissingRecordsOld(self, sessionId):
        """Sends a stream of record metadata for the image being
        replicated, and receives back a stream of records which are
        missing from the remote core.
        """
        return self.session.request('replicationcomms/slave/sessions/%s/records/keys'
                % (sessionId), 'POST')

    def transferMissingRecordsOld(self, sessionId):
        """Sends a stream of raw records to the slave core, the
        list of which is determined by NegotiateMissingRecords.
        """
        return self.session.request('replicationcomms/slave/sessions/%s/records/rawdata'
                % (sessionId), 'POST')

    def endVolumeImageReplicationSessionOld(self, commit):
        """Ends the volume image replication session, optionally
        committing the transferred volume image.
        """
        return self.session.request('replicationcomms/slave/sessions/%s?commit=%s'
                % (commit))

    def endUploadFile(self, uploadSessionId):
        """Ends current upload session and cheks MD5 hash of
        received file.
        """
        return self.session.request('replicationcomms/slave/sessions/%s/'
                % (uploadSessionId), 'POST')

    def cancelUploadFile(self, uploadSessionId):
        """Cancels current upload session."""
        return self.session.request('replicationcomms/slave/sessions/%s/'
                % (uploadSessionId))

    def continueUploadFile(self, uploadSessionId, dataSize):
        """Reads data from slave core in current upload session."""
        return self.session.request('replicationcomms/slave/sessions/%s/data/%s'
                % (uploadSessionId, dataSize), 'POST')

    def startNewVolumeImageReplicationSession(self, data):
        """Starts a replication session with a slave core."""
        return self.session.request('replicationcomms/slave/sessions/new', 'POST',
                    self.getXML(data, 'startVolumeImageReplicationSessionRequest'))

    def updateMasterStorageUsage(self, data):
        """Reports a summary of storage usage on the master core
        to the slave core. This primarily exists to support MSP billing
        needs.
        """
        return self.session.request('replicationcomms/slave/storage', 'PUT',
                    self.getXML(data, 'storageUsageSummary'))

    def getCoreId(self, useCredentials):
        """Tests connection to remote core and returns core ID.
        If useCredentials in true then NTLM authentication used,
        otherwise Anonymous authentication.
        """
        return self.session.request('replicationcomms/slave/validate/?useCredentials=%s'
                % (useCredentials))

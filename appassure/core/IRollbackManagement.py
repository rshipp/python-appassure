"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IRollbackManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/pages/viewpage.action?pageId=2294018
    """

    def generatePartitionPlan(self, data):
        """Generates a partition plan for a given recovery point,
        volume list, and target disks.
        """
        return self.session.request('rollback/autoPartition', 'POST',
                    self.getXML(data, 'autoPartitionRequest'))

    def checkJobByAgentId(self, agentId):
        """Check state of roll-back job using agent id."""
        return self.session.request('rollback/checkJobByAgentId/%s'
                % (agentId), 'POST')

    def checkJobByRrcIp(self, agentIp):
        """Check state of roll-back job using ip address of
        RRC-agent.
        """
        return self.session.request('rollback/checkJobByRrcIp/%s'
                % (agentIp), 'POST')

    def getDatabasesForRemount(self, data):
        """Gets list of databases for remount along with warnings."""
        return self.session.request('rollback/databasesForRemount', 'POST',
                    self.getXML(data, 'rollbackRequest'))

    def validateStoragePoolSettings(self, data):
        """Validates whether Storage Pool feature was enabled on
        the protected machine.
        """
        return self.session.request('rollback/storagepool', 'POST',
                    self.getXML(data, 'rollbackRequest'))

    def getSummaryMetadata(self, data):
        """Gets the disks which are available on a given rollback
        target.
        """
        return self.session.request('rollback/summarymetadata', 'PUT',
                    self.getXML(data, 'rollbackTarget'))

    def startRollback(self, data):
        """Starts a rollback job."""
        return self.session.request('rollback/target', 'POST',
                    self.getXML(data, 'rollbackRequest'))

    def getTargetDisks(self, data):
        """Gets the disks which are available on a given rollback
        target.
        """
        return self.session.request('rollback/targetDisks', 'POST',
                    self.getXML(data, 'rollbackTarget'))

    def getTargetInfo(self, data):
        """Gets the disks and volumes which are available on a
        given rollback target.
        """
        return self.session.request('rollback/targetInfo', 'POST',
                    self.getXML(data, 'rollbackTarget'))

    def getTargetVolumes(self, data):
        """Gets the volumes which are available on a given
        rollback target.
        """
        return self.session.request('rollback/targetVolumes', 'POST',
                    self.getXML(data, 'rollbackTarget'))

    def validateSystemVolumeExistence(self, data):
        """Validate system volume existence."""
        return self.session.request('rollback/validateSystemVolumeExistence', 'POST',
                    self.getXML(data, 'rollbackRequest'))

    def verifyRollbackRequest(self, data):
        """Verify rollback request for volumes and disks."""
        return self.session.request('rollback/verifyRollbackRequest', 'POST',
                    self.getXML(data, 'rollbackRequest'))

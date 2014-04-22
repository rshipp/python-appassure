"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IRollbackManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/pages/viewpage.action?pageId=2294033
    """

    def getRollbackMountDismountStatus(self):
        """Queries the status of the current rollback operation."""
        return self.session.request('rollback/')

    def startRollback(self, data):
        """Initiates a rollback on the agent."""
        return self.session.request('rollback/', 'POST',
                    self.getXML(data, 'startRollbackRequest'))

    def cancelRollback(self):
        """Cancels the running rollback."""
        return self.session.request('rollback/')

    def determinateAutomaticallyAcquiringReplayEngineAddress(self):
        """Determinate if agent can automatically determine
        acquiring ReplayEngine Address.
        """
        return self.session.request('rollback/determinateAutomaticallyAcquiringReplayEngineAddress')

    def startDismounting(self, data):
        """Dismount list of databases."""
        return self.session.request('rollback/dismount', 'PUT',
                    self.getXML(data, 'remountDatabases'))

    def startMounting(self, data):
        """Mount list of databases."""
        return self.session.request('rollback/mount', 'PUT',
                    self.getXML(data, 'remountDatabases'))

    def partitionDisks(self, data):
        """Performs automatic disks partitioning basing on
        partition information in a request object. All existing
        partitions are removed.
        """
        return self.session.request('rollback/partition', 'POST',
                    self.getXML(data, 'partitionRequest'))

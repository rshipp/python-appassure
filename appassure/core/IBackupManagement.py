"""AppAssure 5 Core API"""

from appassure.api import AppAssureAPI

class IBackupManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IBackupManagement
    """

    def startBackup(self, data):
        """Starts a backup."""
        return self.session.request('backup/backup', 'POST',
                    self.getXML(data, 'backupRequest'))

    def updateBackup(self, data, jobId):
        """Updates the job request for an existing backup."""
        return self.session.request('backup/backup/update/%s'
                % (jobId), 'POST',
                    self.getXML(data, 'backupLocation'))

    def getBackupManifests(self, data):
        """Gets the all metadata for an existing backup."""
        return self.session.request('backup/metadataAll', 'POST',
                    self.getXML(data, 'backupLocation'))

    def getBackupManifest(self, data, requestedCoreId):
        """Gets the metadata for an existing core’s backup
        by coreId.
        """
        return self.session.request('backup/metadataByCore/%s'
                % (requestedCoreId), 'POST',
                    self.getXML(data, 'backupLocation'))

    def startRestore(self, data):
        """Starts a restore."""
        return self.session.request('backup/restore', 'POST',
                    self.getXML(data, 'restoreRequest'))

    def updateRestore(self, data, jobId):
        """Updates the job request for an existing backup."""
        return self.session.request('backup/restore/update/%s'
                % (jobId), 'POST',
                    self.getXML(data, 'backupLocation'))

    def verifyBackupLocation(self, data):
        """Verifies whether correct file system path is
        specified as backup location and backup can be put at this
        path.
        """
        return self.session.request('backup/verifyBackupLocation', 'POST',
                    self.getXML(data, 'backupLocation'))

    def verifyRestoreLocation(self, data):
        """Verifies whether backup job has been completed for
        specified location and core.
        """
        return self.session.request('backup/verifyCanStartRestore', 'POST',
                    self.getXML(data, 'backupLocation'))

    def getWaitingJobs(self):
        """Gets a list of waiting backup and restore jobs."""
        return self.session.request('backup/waiting')

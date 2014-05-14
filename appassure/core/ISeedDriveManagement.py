"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class ISeedDriveManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ISeedDriveManagement
    """

    def startConsumeSeedDrive(self, data):
        """Starts consuming recovery points data from
        user-specified seed drive.
        """
        return self.session.request('seedDrive/consume', 'POST',
                    self.getXML(data, 'restoreRequest'))

    def getConsumedSeedDrives(self, agentId):
        """Gets info about seed drives consumed by specified
        replicated agent on the slave core.
        """
        return self.session.request('seedDrive/consumedSeedDrives/%s'
                % (agentId))

    def startCopySeedDrive(self, data):
        """Starts copying recovery points data to user-specified
        seed drive.
        """
        return self.session.request('seedDrive/copy', 'POST',
                    self.getXML(data, 'backupRequest'))

    def getSeedDriveManifest(self, data, coreId):
        """Gets the metadata for an existing seed drive by coreId."""
        return self.session.request('seedDrive/metadataByCore/%s'
                % (coreId), 'POST',
                    self.getXML(data, 'backupLocation i:type="localBackupLocation" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"'))

    def getOutstandingSeedDrives(self):
        """Gets outstanding seed drives on master core which are
        waiting to be consumed on slave cores.
        """
        return self.session.request('seedDrive/outstandingSeedDrives')

    def abandonOutstandingSeedDrive(self, seedDriveId):
        """Deletes seed drive from the list of seed drives which
        are waiting to be consumed.
        """
        return self.session.request('seedDrive/outstandingSeedDrives/%s'
                % (seedDriveId))

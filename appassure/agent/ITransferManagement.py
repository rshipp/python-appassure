"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class ITransferManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ITransferManagement
    """

    def takeSnapshot(self, data):
        """Takes a snapshot of one or more volumes on the agent."""
        return self.session.request('transfer/snapshots', 'POST',
                    self.getXML(data, 'takeSnapshotRequest'))

    def deleteSnapshot(self, data, snapshotSetId):
        """Deletes the snapshot."""
        return self.session.request('transfer/snapshots/%s'
                % (snapshotSetId), 'POST',
                    self.getXML(data, 'deleteSnapshotRequest'))

    def getVolumeAllocatedBlocks(self, snapshotSetId, volumeName):
        """Gets a binary representation of the list of allocated
        blocks on the volume.
        """
        return self.session.request('transfer/snapshots/%s/volumes/%s/blocks/allocated'
                % (snapshotSetId, volumeName))

    def getVolumeChangedBlocks(self, snapshotSetId, volumeName):
        """Gets a binary representation of the list of changed
        blocks on the volume.
        """
        return self.session.request('transfer/snapshots/%s/volumes/%s/blocks/changed'
                % (snapshotSetId, volumeName))

    def getVolumePhysicalDisks(self, snapshotSetId, volumeName):
        """Gets information about the volume's physical layout on
        physical disk (s).
        """
        return self.session.request('transfer/snapshots/%s/volumes/%s/disks'
                % (snapshotSetId, volumeName))

    def getDriverMetadata(self, snapshotSetId, volumeName):
        """Gets the driver metadata for a volume in the snapshot."""
        return self.session.request('transfer/snapshots/%s/volumes/%s/driver'
                % (snapshotSetId, volumeName))

    def setDriverMetadata(self, data, snapshotSetId, volumeName):
        """Sets the driver metadata for a volume in the snapshot.
        Only sets the metadata values which are not set to their default
        values.
        """
        return self.session.request('transfer/snapshots/%s/volumes/%s/driver'
                % (snapshotSetId, volumeName), 'POST',
                    self.getXML(data, 'driverMetadata'))

    def setVolumeEnablement(self, data, snapshotSetId, volumeName):
        """Enables or disables a volume."""
        return self.session.request('transfer/snapshots/%s/volumes/%s/enablement'
                % (snapshotSetId, volumeName), 'POST',
                    self.getXML(data, 'volumeEnablement'))

    def deleteChangeLogsAndMarkClean(self, snapshotSetId, volumeName):
        """Deletes the Replay change logs for the volume."""
        return self.session.request('transfer/snapshots/%s/volumes/%s/logs'
                % (snapshotSetId, volumeName))

    def setGlobalVolumeEnablement(self, data, volumeName):
        """Enables or disables a volume. This method works
        globally since no snapshot ids are needed for it.
        """
        return self.session.request('transfer/volumes/%s/enablement'
                % (volumeName), 'POST',
                    self.getXML(data, 'volumeEnablement'))

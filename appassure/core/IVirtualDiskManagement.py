"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IVirtualDiskManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IVirtualDiskManagement
    """

    def baseFileName(self, id):
        """Gets VHD base file name."""
        return self.session.request('vhd/%s/baseFileName'
                % (id))

    def beginBatch(self, id, target):
        """Begins batch."""
        return self.session.request('vhd/%s/beginBatch/%s'
                % (id, target), 'POST')

    def close(self, id):
        """Closes VHD."""
        return self.session.request('vhd/%s/close'
                % (id))

    def delete(self, id, target):
        """Deletes VHD snapshot or base file."""
        return self.session.request('vhd/%s/delete/%s'
                % (id, target), 'POST')

    def endBatch(self, id):
        """Ends batch."""
        return self.session.request('vhd/%s/endBatch'
                % (id), 'POST')

    def hasSnapshot(self, id):
        """Verifies VHD has snapshot."""
        return self.session.request('vhd/%s/hasSnapshot'
                % (id))

    def read(self, id, target, sectorOffset, sectorLength):
        """Reads raw data from VHD."""
        return self.session.request('vhd/%s/read/%s/%s/%s'
                % (id, target, sectorOffset, sectorLength), 'POST')

    def readCustomMetadata(self, id, target, key):
        """Reads a user-defined custom metadata string."""
        return self.session.request('vhd/%s/readCustomMetadata/%s/%s'
                % (id, target, key), 'POST')

    def sectorSize(self, id):
        """Gets sector size of the VHD."""
        return self.session.request('vhd/%s/sectorSize'
                % (id))

    def snapshotFileName(self, id):
        """Gets VHD snapshot file name."""
        return self.session.request('vhd/%s/snapshotFileName'
                % (id))

    def takeSnapshot(self, id):
        """Takes VHD snapshot."""
        return self.session.request('vhd/%s/takeSnapshot'
                % (id))

    def totalSectorCapacity(self, id):
        """Gets VHD capacity."""
        return self.session.request('vhd/%s/totalSectorCapacity'
                % (id))

    def translateSectorOffsetToChsTuple(self, id, sectorOffset):
        """Translates sector offset to chs tuple."""
        return self.session.request('vhd/%s/translateSectorOffsetToChsTuple?sectorOffset=%s'
                % (id, sectorOffset))

    def write(self, id, target, sectorOffset, sectorLength):
        """Writes raw data to VHD."""
        return self.session.request('vhd/%s/write/%s/%s/%s'
                % (id, target, sectorOffset, sectorLength), 'POST')

    def writeCustomMetadata(self, id, target, value):
        """Reads a user-defined custom metadata string."""
        return self.session.request('vhd/%s/writeCustomMetadata/%s/%s?value=%s'
                % (id, target, value), 'POST')

    def create(self, path, bytesCapacity, bytesPerSector,
            containsBootSystemVolume, preallocate):
        """Creates VHD."""
        return self.session.request('vhd/createVhd?path=%s&bytesCapacity=%s&bytesPerSector=%s&containsBootSystemVolume=%s&preallocate=%s'
                % (path, bytesCapacity, bytesPerSector,
                      containsBootSystemVolume, preallocate), 'PUT')

    def open(self, path):
        """No summary."""
        return self.session.request('vhd/openVhd?path=%s'
                % (path), 'PUT')

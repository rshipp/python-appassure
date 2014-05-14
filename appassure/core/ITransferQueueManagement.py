"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class ITransferQueueManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ITransferQueueManagement
    """

    def getActiveQueueEntries(self):
        """Gets the active entries in the transfer queue."""
        return self.session.request('xfer/queue/activeEntries')

    def getQueueConfiguration(self):
        """Gets the configuration of the transfer queue."""
        return self.session.request('xfer/queue/config')

    def setQueueConfiguration(self, data):
        """Sets the configuration of the transfer queue."""
        return self.session.request('xfer/queue/config', 'POST',
                    self.getXML(data, 'config'))

    def getQueueContents(self):
        """Gets the contents of the transfer queue."""
        return self.session.request('xfer/queue/entries')

    def cancelAllTransfers(self):
        """Cancels every transfer in the queue."""
        return self.session.request('xfer/queue/entries')

    def getEntryInfo(self, transferid):
        """Gets the info for a specific transfer queue entry."""
        return self.session.request('xfer/queue/entries/%s'
                % (transferid))

    def cancelTransfer(self, transferid):
        """Cancels the transfer queue entry identified by the
        transfer ID.
        """
        return self.session.request('xfer/queue/entries/%s'
                % (transferid))

    def adjustTransferPriority(self, data, transferid):
        """Adjusts the priority of the transfer in the queue."""
        return self.session.request('xfer/queue/entries/%s'
                % (transferid), 'POST',
                    self.getXML(data, 'changeXferPriority'))

    def getFailedQueueEntries(self):
        """Gets the failed entries in the transfer queue."""
        return self.session.request('xfer/queue/failedEntries')

    def getPendingQueueEntries(self):
        """Gets the pending entries in the transfer queue."""
        return self.session.request('xfer/queue/pendingEntries')

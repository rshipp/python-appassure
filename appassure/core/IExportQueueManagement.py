"""AppAssure 5 Core API"""

from appassure.appassureapi import AppAssureAPI

class IExportQueueManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IExportQueueManagement
    """

    def getConfiguration(self):
        """Gets the configuration of the VM export queue."""
        return self.session.request('export/queue/config')

    def setConfiguration(self, data):
        """Sets the configuration of the VM export queue."""
        return self.session.request('export/queue/config', 'POST',
                    self.getXML(data, 'config'))

    def getQueueContents(self):
        """Gets the contents of the export queue."""
        return self.session.request('export/queue/entries')

    def cancelAllExports(self):
        """Cancels every export in the queue."""
        return self.session.request('export/queue/entries', 'DELETE')

    def getEntryInfo(self, exportid):
        """Gets the info for a specific export queue entry."""
        return self.session.request('export/queue/entries/%s'
                % (exportid))

    def cancelExports(self, data):
        """Cancels the export queue entrys identified by the
        export IDs.
        """
        return self.session.request('export/queue/entries/cancel', 'POST',
                    self.getXML(data, 'cancelExportsRequest'))

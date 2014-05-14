"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class ILoggingManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ILoggingManagement
    """

    def allRegisteredTraceLogs(self):
        """Gets all registered trace logs entries."""
        return self.session.request('logs/allRegisteredTraceLogs')

    def getEnabledTraceLogs(self):
        """Gets enabled trace logs entries."""
        return self.session.request('logs/enabledTraceLogs')

    def enableTraceLog(self, data):
        """Enables specified trace log."""
        return self.session.request('logs/enableTraceLog', 'PUT',
                    self.getXML(data, 'enabledTraceLog'))

    def setEnabledTraceLogs(self, data):
        """Applies new set of enabled trace logs."""
        return self.session.request('logs/enableTraceLogs', 'POST',
                    self.getXML(data, 'enableTraceLogsRequest'))

    def traceLogSuggestions(self):
        """Gets suggestions to enable trace logs."""
        return self.session.request('logs/traceLogSuggestions')

    def unregisterTraceLogs(self, data):
        """Unregisteres trace log by filter name."""
        return self.session.request('logs/unregisterTraceLogs', 'POST',
                    self.getXML(data, 'disableTraceLogsRequest'))

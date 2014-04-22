"""AppAssure 5 Core API"""

from appassure.api import AppAssureAPI

class ICoreDiagnosticsManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ICoreDiagnosticsManagement
    """

    def uploadLogSessions(self):
        """Uploads the current logs for this core and all
        online, protected agents to Gibraltar
        (http://www.gibraltarsoftware.com/) via a background job;
        returns the ID of that job.
        """
        return self.session.request('corediag/logs/', 'POST')

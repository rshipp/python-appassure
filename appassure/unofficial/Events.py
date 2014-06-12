"""AppAssure 5 REST API

Unofficial, undocumented web interface API endpoints.
"""

from appassure.api import AppAssureAPI

class Events(AppAssureAPI):
    """No documentation available.

    Methods in this class were reverse engineered from the AppAssure
    administrative web interface.
    """

    def taskMonitor(self, task_id):
        """Get task information."""
        return self.session.http.post(
                '%s/apprecovery/admin/Events/TaskMonitor' % self.session.baseurl,
                data={'id': task_id},
                auth=self.session.auth
                )

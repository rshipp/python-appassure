"""AppAssure 5 Core API"""

from appassure.api import AppAssureAPI

class ICoreMetadataManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ICoreMetadataManagement
    """

    def getCurrent(self):
        """Gets the current Core metadata."""
        return self.session.request('metadata/')

    def getCached(self):
        """Gets cached Core metadata."""
        return self.session.request('metadata/cached')

    def getCachedSummary(self):
        """Gets cached Core summary metadata."""
        return self.session.request('metadata/cachedsummary')

    def getCurrentSummary(self):
        """Gets the current Core summary metadata."""
        return self.session.request('metadata/summary')

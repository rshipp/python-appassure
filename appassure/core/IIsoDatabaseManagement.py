"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IIsoDatabaseManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IIsoDatabaseManagement
    """

    def getAllIsoEntries(self):
        """Returns full list of ISO files which have been created
        previously.
        """
        return self.session.request('bootcdbuilder/isos')

    def deleteIsoEntry(self, entryId):
        """Asks service to delete particular entry."""
        return self.session.request('bootcdbuilder/isos/%s'
                % (entryId))

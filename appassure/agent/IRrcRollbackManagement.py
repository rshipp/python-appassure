"""AppAssure 5 REST API"""

from appassure.appassureapi import AppAssureAPI

class IRrcRollbackManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IRrcRollbackManagement
    """

    def fixBootable(self, data):
        """Performs post processing of boot volume in order to
        correct boot manager and make volume bootable after BMR. This
        method is for internal usage only and should not be called by
        users.
        """
        return self.session.request('rollback/fixBoot', 'PUT',
                    self.getXML(data, 'fixBootRequest'))

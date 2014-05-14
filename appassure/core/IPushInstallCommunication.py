"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IPushInstallCommunication(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IPushInstallCommunication
    """

    def setInstallationProgress(self, jobId, messageType, progress):
        """This method is called by push install functionality on
        in order to track progress of remote agent installation. This
        method is for internal usage only. {message}.
        """
        return self.session.request('pushinstallcomm/setProgress/jobs/%s/%s/%s/'
                % (jobId, messageType, progress), 'POST')

    def getInstallationStatus(self, jobId):
        """Gets installation progress of child push install job."""
        return self.session.request('pushinstallcomm/status/jobs/%s'
                % (jobId))

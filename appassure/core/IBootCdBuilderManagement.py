"""AppAssure 5 Core API"""

from appassure.api import AppAssureAPI

class IBootCdBuilderManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IBootCdBuilderManagement
    """

    def getDefaultOutputPath(self):
        """Gets the default path were resulting ISO image
        will be put if output path was not specified explicitly.
        """
        return self.session.request('bootcdbuilder/defaults')

    def startBuildingIso(self, data):
        """Starts new ISO image building task."""
        return self.session.request('bootcdbuilder/start', 'POST',
                    self.getXML(data, 'bootCdBuilderRequest'))

    def validateDriverPackages(self, data):
        """Performs validation of specified driver packages."""
        return self.session.request('bootcdbuilder/validate', 'POST',
                    self.getXML(data, 'driverPackageValidationRequest'))

    def verifyBuildingIsoParameters(self, data):
        """Verifies that ISO parameters are built properly."""
        return self.session.request('bootcdbuilder/verify', 'POST',
                    self.getXML(data, 'bootCdBuilderParams'))

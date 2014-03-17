"""AppAssure 5 Core API"""

from appassure.appassureapi import AppAssureAPI

class IExportSchedulerManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IExportSchedulerManagement
    """

    def forceExport(self, data, agentId):
        """Immediately starts VM export of a recovery point 
        which corresponds to specified agent. The recovery point and 
        resulting VM type (Workstation, EC2 or ESXi) should be 
        specified in the request instance.
        """
        return self.session.request('export/schedule/%s/export' 
                % (agentId), 'POST', 
                    self.getXML(data, 'ForceExport'))

    def getAgentExportConfiguration(self, agentId):
        """Gets the export configuration for the agent."""
        return self.session.request('export/schedule/%s/pgs' 
                % (agentId))

    def setAgentExportConfiguration(self, data, agentId):
        """Sets the export configuration for the agent."""
        return self.session.request('export/schedule/%s/pgs' 
                % (agentId), 'PUT', 
                    self.getXML(data, 'exportConfig'))

    def deleteAgentExportConfiguration(self, agentId):
        """Deletes the export configuration for the agent."""
        return self.session.request('export/schedule/%s/pgs' 
                % (agentId))

    def getAllAgentsExportStatus(self):
        """Gets a summary of the export status for every 
        agent on the core for which Virtual Standby is enabled.
        """
        return self.session.request('export/schedule/agents/all')

    def getAllAgentsExportConfiguration(self):
        """Gets the export configuration for the agent."""
        return self.session.request('export/schedule/agents/allExportConfig')

    def getAllEC2Credentials(self):
        """Gets all EC2 credentials."""
        return self.session.request('export/schedule/ec2/credentials')

    def updateEC2Credentials(self, data):
        """Creates or updates EC2 credential."""
        return self.session.request('export/schedule/ec2/credentials', 'POST', 
                    self.getXML(data, 'ec2Credential'))

    def getEC2Credentials(self, key):
        """Gets specific EC2 credentials."""
        return self.session.request('export/schedule/ec2/credentials/%s' 
                % (key))

    def deleteEC2Credentials(self, key):
        """Deletes EC2 credential."""
        return self.session.request('export/schedule/ec2/credentials/%s' 
                % (key))

    def getEc2Environment(self, credentialKey):
        """Gets EC2 security information specific to an 
        environment whose method is being called.
        """
        return self.session.request('export/schedule/ec2/environment/%s' 
                % (credentialKey))

    def validateEC2Credentials(self, data):
        """Validates an EC2 credential."""
        return self.session.request('export/schedule/ec2/validate', 'POST', 
                    self.getXML(data, 'ec2Credential'))

    def getGroupAgentsExportStatus(self, groupId):
        """Gets a summary of the export status for every 
        agent in the given group for which Virtual Standby is 
        enabled.
        """
        return self.session.request('export/schedule/groups/%s/all' 
                % (groupId))

    def validateHyperVCredentials(self, data):
        """Validates an Hyper-V credentials."""
        return self.session.request('export/schedule/hyperv/credentials', 'POST', 
                    self.getXML(data, 'hypervCredential'))

    def validateHyperVDiskExists(self, data, path):
        """Validates Hyper-V disk exists."""
        return self.session.request('export/schedule/hyperv/location/%s' 
                % (path), 'POST', 
                    self.getXML(data, 'hypervCredential'))

    def validateHyperVRoleIsInstalled(self, data):
        """Validates Hyper-V credentials."""
        return self.session.request('export/schedule/hyperv/role', 'POST', 
                    self.getXML(data, 'hypervCredential'))

    def getFreeSpaceOnNetworkShare(self, data):
        """Validates a UNC share path."""
        return self.session.request('export/schedule/uncshare/validate', 'POST', 
                    self.getXML(data, 'virtualMachineLocation i:type="esxlocation" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"'))

    def validateExportLocation(self, data):
        """Validates location for virtual machine."""
        return self.session.request('export/schedule/vm/location/validate', 'POST', 
                    self.getXML(data, 'virtualMachineLocation i:type="esxlocation" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"'))

    def getVSphereServerInformation(self, data):
        """Retrieves the details about a VSphere server for 
        UI functionality.
        """
        return self.session.request('export/schedule/vsphere/info', 'POST', 
                    self.getXML(data, 'esxServerSummaryRequest'))

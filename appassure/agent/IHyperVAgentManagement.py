"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IHyperVAgentManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/pages/viewpage.action?pageId=3965666
    """

    def getAvailableVirtualNetworks(self, virtualMachineId):
        """Gets a list of virtual network adapters on Hyper-V
        server available for a virtual machine.
        """
        return self.session.request('hypervagent/%s/availablevirtualnetworks'
                % (virtualMachineId))

    def setProcessorCount(self, virtualMachineId, processorCount):
        """Changes number of virtual CPUs in current virtual
        machine.
        """
        return self.session.request('hypervagent/%s/cpu/%s'
                % (virtualMachineId, processorCount), 'PUT')

    def getVirtualDisks(self, virtualMachineId):
        """Gets a list of virtual disks currently attached to
        current virtual machine.
        """
        return self.session.request('hypervagent/%s/disks'
                % (virtualMachineId))

    def detachVirtualDisk(self, virtualMachineId, diskPath):
        """Detaches a virtual disk from current virtual machine."""
        return self.session.request('hypervagent/%s/disks/%s'
                % (virtualMachineId, diskPath))

    def attachVirtualDisk(self, virtualMachineId, diskPath, storageController):
        """Attaches a virtual disk to current virtual machine."""
        return self.session.request('hypervagent/%s/disks/%s/%s'
                % (virtualMachineId, diskPath, storageController), 'PUT')

    def addDvdDrive(self, virtualMachineId):
        """Adds a DVD drive to current virtual machine."""
        return self.session.request('hypervagent/%s/dvd'
                % (virtualMachineId), 'PUT')

    def endSession(self, virtualMachineId):
        """Tells Hyper-V Agent to finish session with the virtual
        machine.
        """
        return self.session.request('hypervagent/%s/endsession'
                % (virtualMachineId))

    def insertIntegrationServices(self, virtualMachineId):
        """Mounts the integration services setup disk."""
        return self.session.request('hypervagent/%s/integrationservices'
                % (virtualMachineId), 'PUT')

    def addIsoImage(self, virtualMachineId, isoPath):
        """Adds an ISO image to a DVD drive. If DVD drive doesn't
        exist - creates it.
        """
        return self.session.request('hypervagent/%s/iso/%s'
                % (virtualMachineId, isoPath), 'PUT')

    def getVirtualMachineName(self, virtualMachineId):
        """Gets name of current virtual machine."""
        return self.session.request('hypervagent/%s/name'
                % (virtualMachineId))

    def renameVirtualMachine(self, virtualMachineId, newVirtualMachineName):
        """Renames current virtual machine."""
        return self.session.request('hypervagent/%s/newname/%s'
                % (virtualMachineId, newVirtualMachineName), 'PUT')

    def addNetworkAdapter(self, virtualMachineId, networkAdapterName):
        """Adds new network adapter to current virtual machine."""
        return self.session.request('hypervagent/%s/nic/%s'
                % (virtualMachineId, networkAdapterName), 'PUT')

    def setRamMegabytes(self, virtualMachineId, ramValue):
        """Changes amount of RAM in current virtual machine."""
        return self.session.request('hypervagent/%s/ram/%s'
                % (virtualMachineId, ramValue), 'PUT')

    def verifyConnection(self):
        """Verifies connection to the running HyperV Agent."""
        return self.session.request('hypervagent/connect')

    def attachToExistentVirtualMachine(self, data):
        """Attaches to an existent virtual machine specified in
        request parameter.
        """
        return self.session.request('hypervagent/existent', 'POST',
                    self.getXML(data, 'hyperVVirtualMachineRequest'))

    def deleteVirtualMachine(self, virtualMachineId):
        """Deletes current virtual machine and detaches from it."""
        return self.session.request('hypervagent/existent/%s'
                % (virtualMachineId))

    def createNewVirtualMachineAndAttach(self, data):
        """Creates new virtual machine specified in request
        parameter.
        """
        return self.session.request('hypervagent/new', 'POST',
                    self.getXML(data, 'hyperVVirtualMachineRequest'))

    def startNewFileTransmitSession(self, data):
        """Starts new file transmit session."""
        return self.session.request('exchangedll/newsession/', 'POST',
                    self.getXML(data, 'fileTransmitRequest'))

    def endTransmitFile(self, fileTransmitSessionId):
        """Ends current transmit session."""
        return self.session.request('exchangedll/sessions/%s/'
                % (fileTransmitSessionId), 'POST')

    def cancelTransmitFile(self, fileTransmitSessionId):
        """Cancels current transmit session."""
        return self.session.request('exchangedll/sessions/%s/'
                % (fileTransmitSessionId))

    def continueTransmitFile(self, fileTransmitSessionId, bytesToRead):
        """Reads data from agent in current transmit session."""
        return self.session.request('exchangedll/sessions/%s/data/%s'
                % (fileTransmitSessionId, bytesToRead), 'POST')

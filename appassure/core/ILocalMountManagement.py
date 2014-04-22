"""AppAssure 5 Core API"""

from appassure.api import AppAssureAPI

class ILocalMountManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ILocalMountManagement
    """


    def startMount(self, data):
        """Starts mounting a specified recovery point.

        data must be a correctly formatted dictionary containing the
        information described at
        http://docs.appassure.com/display/AA50D/ILocalMountManagement#ILocalMountManagement-StartMount

        The following is an example request dict object:

            {
                'agentIds': {
                    'agentId': '1627aea5-8e0a-4371-9022-9b504344e724',
                    'agentId': '1627aea5-8e0a-4371-9022-9b504344e724',
                    },
                'isNightlyJob': 'true',
                'jobId': '1627aea5-8e0a-4371-9022-9b504344e724',
                'mountPoint': 'String content',
                'recoveryPoint': 'String content',
                'shareAllowedGroup': 'String content',
                'shareName': 'String content',
                'type': 'None',
                'volumeImagesToMount': {
                    'string xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays"':
                        'String content',
                    'string xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays"':
                        'String content',
                },
            }

        Note that the validity of the dict will not be checked by
        this function. If it is invalid, AppAssureSession or
        AppAssureAPI may raise some exception (which you should
        catch and deal with), or everything might continue happily,
        and this function will return invalid data.
        """
        return self.session.request('mounts', 'POST', self.getXML(data,
                    'mountRequest'))

    def getMounts(self):
        """Gets the list of currently mounted volumes."""
        return self.session.request('mounts')

    def getAgentMounts(self, agentId):
        """Gets the list of currently mounted volumes which
        came from a a specific agent.

        agentId must be a valid UUID of an agent that exists on the
        Core server.
        """
        return self.session.request('mounts/agents/%s' % agentId)

    def dismountAllAgent(self, agentId):
        """Dismounts all mounted volumes which came from a
        specific agent.

        agentId must be a valid UUID of an agent that exists on the
        Core server.
        """
        return self.session.request('mounts/agents/%s/allvolumes' %
                agentId, 'DELETE')

    def dismountAll(self):
        """Dismounts all mounted volumes."""
        return self.session.request('mounts/allvolumes' % agentId,
                'DELETE')

    def getMountOptions(self):
        """Gets options for where to mount recovery points."""
        return self.session.request('mounts/options')

    def dismount(self, mountedVolumeName):
        """Dismounts one mounted volume.

        mountedVolumeName must be a valid name of a mounted volume on
        the Core server.
        """
        return self.session.request('mounts/volume/%s' %
                monutedVolumeName, 'DELETE')

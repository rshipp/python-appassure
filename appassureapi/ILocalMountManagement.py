"""AppAssure 5 Core API
   ILocalMountManagement
"""

from appassureapi import AppAssureAPI

class ILocalMountManagement(AppAssureAPI):
    
    def StartMount(self, data):
        """Summary: Starts mounting a specified recovery point.
           URI: mounts/
           HTTP Method: POST

           data must be a correctly formatted dictionary containing the
           information described at
           http://docs.appassure.com/display/AA50D/ILocalMountManagement#ILocalMountManagement-StartMount
           
           The following is an example request dict object:

                {
                    'agentIds': {
                        'agentId':
                            '1627aea5-8e0a-4371-9022-9b504344e724',
                        'agentId':
                            '1627aea5-8e0a-4371-9022-9b504344e724',
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
                    'mountRequest xmlns="http://apprecovery.com/management/api/2010/05"'))

    def GetMounts(self):
        """Summary: Gets the list of currently mounted volumes.
           URI: mounts/
           HTTP Method: GET 
        """
        return self.session.request('mounts')

    def GetAgentMounts(self, agentId):
        """Summary: Gets the list of currently mounted volumes which
            came from a a specific agent.
           URI: mounts/agents/{agentId}
           HTTP Method: GET

           agentId must be a valid UUID of an agent that exists on the
           Core server.
        """
        return self.session.request('mounts/agents/%s' % agentId)

    def DismountAllAgent(self, agentId):
        """Summary: Dismounts all mounted volumes which came from a
            specific agent.
           URI: mounts/agents/{agentId}/allvolumes
           HTTP Method: DELETE

           agentId must be a valid UUID of an agent that exists on the
           Core server.
        """
        return self.session.request('mounts/agents/%s/allvolumes' %
                agentId, 'DELETE')

    def DismountAll(self):
        """Summary: Dismounts all mounted volumes.
           URI: mounts/allvolumes
           HTTP Method: DELETE
        """
        return self.session.request('mounts/allvolumes' % agentId,
                'DELETE')

    def GetMountOptions(self):
        """Summary: Gets options for where to mount recovery points.
           URI: mounts/options
           HTTP Method: GET
        """
        return self.session.request('mounts/options')

    def Dismount(self, mountedVolumeName):
        """Summary: Dismounts one mounted volume.
           URI: mounts/volume/{mountedVolumeName}
           HTTP Method: DELETE

           mountedVolumeName must be a valid name of a mounted volume on
           the Core server.
        """
        return self.session.request('mounts/volume/%s' %
                monutedVolumeName, 'DELETE')

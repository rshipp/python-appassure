"""AppAssure 5 Core API
   ILocalMountManagemeht
"""

from appassureapi import AppAssureAPI

class ILocalMountManagement(AppAssureAPI):
    
    def StartMount(self):
        """Summary: Starts mounting a specified recovery point.
           URI: mounts/
           HTTP Method: POST
        """

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

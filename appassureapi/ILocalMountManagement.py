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

    def GetAgentMounts(self):
        """Summary: Gets the list of currently mounted volumes which
            came from a a specific agent.
           URI: mounts/agents/{agentId}
           HTTP Method: GET
        """


    def DismountAllAgent(self):
        """Summary: Dismounts all mounted volumes which came from a
            specific agent.
           URI: mounts/agents/{agentId}/allvolumes
           HTTP Method: DELETE
        """


    def DismountAll(self):
        """Summary: Dismounts all mounted volumes.
           URI: mounts/allvolumes
           HTTP Method: DELETE
        """


    def GetMountOptions(self):
        """Summary: Gets options for where to mount recovery points.
           URI: mounts/options
           HTTP Method: GET
        """


    def Dismount(self):
        """Summary: Dismounts one mounted volume.
           URI: mounts/volume/{mountedVolumeName}
           HTTP Method: DELETE
        """


"""AppAssure 5 Core API"""

from appassure.appassureapi import AppAssureAPI

class IClustersManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IClustersManagement
    """

    def convertAgentToClusterNode(self, agentId):
        """Convert regular agent to cluster node."""
        return self.session.request('clusters/%s/convertToNode'
                % (agentId), 'POST')

    def addClusterNodeAgent(self, data, clusterId):
        """Add cluster node to existing cluster."""
        return self.session.request('clusters/%s/nodes/new'
                % (clusterId), 'POST',
                    self.getXML(data, 'addAgentRequest'))

    def convertClusterNodeToAgent(self, clusterNodeId):
        """Convert cluster node to regular agent."""
        return self.session.request('clusters/%s/convertToAgent'
                % (clusterNodeId), 'POST')

    def getClusterNodes(self, clusterAgentId):
        """Gets a list of cluster nodes for specified cluster
        agent.
        """
        return self.session.request('clusters/clusterNodes/%s'
                % (clusterAgentId))

    def addClusterAgent(self, data):
        """Protect the cluster with nodes."""
        return self.session.request('clusters/new', 'PUT',
                    self.getXML(data, 'addClusterRequest'))

    def getReplicatedClusterNodes(self, clusterAgentId):
        """Gets a list of replicated cluster nodes for
        specified cluster agent.
        """
        return self.session.request('clusters/replicatedClusterNodes/%s'
                % (clusterAgentId))

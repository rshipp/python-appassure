"""AppAssure 5 Core API"""

from appassure.appassureapi import AppAssureAPI

class IDatabaseStorageManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IDatabaseStorageManagement
    """

    def getDatabaseStorageConfiguration(self):
        """Gets database storage configuration (like database 
        server connection settings, database data retention period, 
        connection timeout).
        """
        return self.session.request('databaseStorage/configuration')

    def setDatabaseStorageConfiguration(self, data):
        """Sets database storage configuration (like database 
        server connection settings, database data retention period, 
        connection timeout).
        """
        return self.session.request('databaseStorage/configuration', 'PUT', 
                    self.getXML(data, 'databaseStorageConfiguration'))

    def testConnection(self, data):
        """Tests connection with database storage instance 
        using specified connection settings.
        """
        return self.session.request('databaseStorage/connection', 'POST', 
                    self.getXML(data, 'databaseServerConnectionSettings'))

    def getDefaultDatabaseStorageConfiguration(self):
        """Gets default database storage configuration."""
        return self.session.request('databaseStorage/defaults')

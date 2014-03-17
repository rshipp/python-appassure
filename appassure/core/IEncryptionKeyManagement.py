"""AppAssure 5 Core API"""

from appassure.appassureapi import AppAssureAPI

class IEncryptionKeyManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IEncryptionKeyManagement
    """

    def getKeys(self):
        """Gets the list of encryption keys."""
        return self.session.request('encryption/')

    def create(self, data):
        """Creates a new key with the specified name and
        passphrase.
        """
        return self.session.request('encryption/', 'POST',
                    self.getXML(data, 'newKeyRequest'))

    def update(self, data, keyId):
        """Updates an existing key."""
        return self.session.request('encryption/%s'
                % (keyId), 'PUT',
                    self.getXML(data, 'encryptionKeyBasic'))

    def export(self, keyId):
        """Exports a key."""
        return self.session.request('encryption/%s'
                % (keyId))

    def hasPassphrase(self, keyId):
        """Returns response of whether a passphrase exists
        for the specified key.
        """
        return self.session.request('encryption/%s/passphrase'
                % (keyId))

    def setPassphrase(self, data, keyId):
        """Changes the passphrase for the specified key."""
        return self.session.request('encryption/%s/passphrase'
                % (keyId), 'POST',
                    self.getXML(data, 'newPassphraseRequest'))

    def serializedExport(self, keyId):
        """Returns serialized binary representation of
        encryption key by given key ID.
        """
        return self.session.request('encryption/%s/serialized'
                % (keyId))

    def setTemporaryPassphrase(self, data, keyId):
        """Sets a temporary passphrase."""
        return self.session.request('encryption/%s/temppassphrase'
                % (keyId), 'POST',
                    self.getXML(data, 'newTemporaryPassphraseRequest'))

    def import(self, data):
        """Imports an exported key."""
        return self.session.request('encryption/import', 'POST',
                    self.getXML(data, 'exportedKey'))

    def findMissing(self, data):
        """Returns a list of the key IDs for a specified
        input list that have no passphrases.
        """
        return self.session.request('encryption/missingpassphrases', 'POST',
                    self.getXML(data, 'keyidcollection'))

    def serializedImport(self, data):
        """Imports an encryption key by given serialized
        binary representation.
        """
        return self.session.request('encryption/serimport', 'POST',
                    self.getXML(data, 'setExportedKey'))

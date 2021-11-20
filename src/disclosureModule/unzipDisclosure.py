# Disclosure zip file.
import zipfile
import os

class zipDisclosure:
    
    # require
    # docId: string
    # return: none
    def unzipDisclosure (self, docId):
        zipFile = zipfile.ZipFile(self.generateZipFilePath(docId))
        zipFile.extractall(os.path.expanduser("~") + "/disclosure-search/disclosureFiles/")
        zipFile.close()

    # require
    # docId: string
    # return: string
    # This Zip File Name is for Mac. Other OS is not supported.
    def generateZipFilePath (self, docId):
        return os.path.expanduser("~") + "/disclosure-search/disclosureFiles/" + docId + ".zip"

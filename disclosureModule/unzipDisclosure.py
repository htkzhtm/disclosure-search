# Disclosure zip file.
import zipfile
import os

class zipDisclosure:
    
    # require
    # docId: string
    # return: none
    def unzipDisclosure (self, docId):
        zipFile = zipfile.ZipFile('path')
        zipFile.extractall('path')
        zipFile.close()

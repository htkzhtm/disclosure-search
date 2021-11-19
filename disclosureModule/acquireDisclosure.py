# Get the disclosure used by EDINET API.
# XBRL or PDF function
import requests
import os

class disAcquirer:
    baseURL = "https://disclosure.edinet-fsa.go.jp/api/v1/documents/"
    typeZip = 1
    typePDF = 2

    # require: docId (EDINET managed number)
    # return : None
    def aqquireDisclosurePDF (self, docId):
        self.generateFile(docId, self.typePDF)

    # require: docId (EDINET managed number)
    # return : None
    def aqquireDisclosureZip (self, docId):
        self.generateFile(docId, self.typeZip)

    # require
    # docId: docId (EDINET managed number)
    # typeId: Zip:1 PDF:2 This parameter is specified by the specifications of EDINET.

    # return : None
    def generateFile (self, docId, typeId):
        url = self.baseURL + docId
        params = {
            "type" : typeId
        }

        # Call the API to get the file.
        # File path spec is thinking. Now, repo exists on home directory
        res = requests.get(url, params=params, verify=False)
        filename = os.path.expanduser("~") + "/disclosure-search/disclosureFiles/" + docId + (".zip" if typeId == self.typeZip else ".pdf")
        
        # Write
        self.makedisclosureFilingDir()
        if res.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in res.iter_content(chunk_size=1024):
                    f.write(chunk)
        else:
            print("Response was failed. Check the EDINET specification doc.")

    # Make directory for disclosure
    # require none
    # return none
    def makedisclosureFilingDir (self):
        if not os.path.exists(os.path.expanduser("~") + "/disclosure-search/disclosureFiles"):
            os.mkdir(os.path.expanduser("~") + "/disclosure-search/disclosureFiles")

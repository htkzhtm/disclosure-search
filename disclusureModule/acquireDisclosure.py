# Get the disclosure used by EDINET API.
# XBRL or PDF function
import requests

class disAcquirer:
    baseURL = "https://disclosure.edinet-fsa.go.jp/api/v1/documents/"

    # require: dodId (EDINET managed number)
    # return : None
    def aqquireDisclosurePDF (self, docId):
        url = self.baseURL + docId
        params = {
            "type" : 2
        }

        res = requests.get(url, params=params, verify=False)
        filename = docId + ".pdf"
        # Write
        if res.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in res.iter_content(chunk_size=1024):
                    f.write(chunk)
        else:
            print("Response was failed. Check the EDINET specification doc.")

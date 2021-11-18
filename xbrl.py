import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

# DocID
docid = "XXXXX"

url = "https://disclosure.edinet-fsa.go.jp/api/v1/documents/" + docid

# 1:zip 2:pdf
params = {
  "type" : 1
}

# ex:zip
filename = docid + ".zip"

res = requests.get(url, params=params, verify=False)

# Write
if res.status_code == 200:
  with open(filename, 'wb') as f:
    for chunk in res.iter_content(chunk_size=1024):
      f.write(chunk)
else:
    print("Response was failed. Check the EDINET specification doc.")

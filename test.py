import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

url = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json"

params = {
  "date" : "2021-11-11",
  "type" : 2
}

res = requests.get(url, params=params, verify=False)

print(res.text)


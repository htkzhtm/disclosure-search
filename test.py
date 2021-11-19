import sys
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

# Specify the date. Not rigorously checked, because this limitation will be abolished.
if len(sys.argv) < 2:
  print("Specify the date(YYYY-MM-DD) command line arg.")
  sys.exit()

# Get the Disclosures submitted on YYYY-MM-DD
jsonData = requests.get(
  url = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json",
  params = {
    "date" : sys.argv[1],
    "type" : 2
  },
  verify=False
).json()
if (jsonData["metadata"]["message"] == "404"):
  print ("Maybe illegal date. Check your insert date. Or, disclosure submitted this date may not be existed.")
  sys.exit()

# Search the securities report submitted by listed company.
disclosureList = []
for num in range(len(jsonData["results"])):
  if (jsonData["results"][num]["ordinanceCode"] == "010" and
    jsonData["results"][num]["formCode"] == "030000" and
    jsonData["results"][num]["secCode"] != None
  ):
    disclosureList.append({
      "secCode": jsonData["results"][num]["secCode"],
      "filerName": jsonData["results"][num]["filerName"],
      "dodId": jsonData["results"][num]["docID"],
      "docDescription": jsonData["results"][num]["docDescription"]
    })

print (disclosureList)

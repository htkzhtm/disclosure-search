# Disclosure search used by EDINETAPI.
# This module is search only. Downdload function is another its.

import sys
import requests
import urllib3
import datetime
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class disSearcher:
    # If quarterly disclosure, 90 days may be fine.
    # This specification may be changed.
    dayOffset = 1

    # Japanese company often submits the securities report on June.
    # currentTime = datetime.datetime.now() - datetime.timedelta(days = 150)
    currentTime = datetime.datetime.now()

    # Matching disclosure list.
    disclosureList = []

    # constructor is not existed.
    # def __init__(self):


    # require: none
    # return: [] {secCode, filerName, dodId, docDescription}

    # secCode: The disclosure number managed by EDINET.
    # dodId: The securities code.
    # filerName: A submitter. This name is often a company name.
    # docDescription: Description of disclosure.
    def searchDis (self):
        # while example. This spec wad abolished.
        # while currentTime.date() > datetime.date(2021, 10, 30):

        for delta in range(0, self.dayOffset + 1):
            print("Disclosure in", (self.currentTime - datetime.timedelta(days = delta)).date()) 

            # Get the Disclosures submitted on YYYY-MM-DD
            jsonData = requests.get(
                url = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json",
                params = {
                    "date" : (self.currentTime - datetime.timedelta(days = delta)).date(),
                    "type" : 2
                },
                verify=False
            ).json()
            if (jsonData["metadata"]["message"] == "404"):
                print ("A illegal date may be included. Check your insert date.")
                sys.exit()

            # Search the securities report submitted by listed company.
            for num in range(len(jsonData["results"])):
                if (jsonData["results"][num]["ordinanceCode"] == "010" and
                    jsonData["results"][num]["formCode"] == "030000" and
                    jsonData["results"][num]["secCode"] != None
                ):
                    self.disclosureList.append({
                        "secCode": jsonData["results"][num]["secCode"],
                        "filerName": jsonData["results"][num]["filerName"],
                        "dodId": jsonData["results"][num]["docID"],
                        "docDescription": jsonData["results"][num]["docDescription"]
                    })
        return self.disclosureList

# Disclosure search used by EDINETAPI.
# This module is search only. Downdload function is another its.

import sys
import requests
import urllib3
# import pprint
import datetime
from ..disclosureSpecification import inspection as dsi
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class disSearcher:
    # If quarterly disclosure, 120 days may be fine.
    # This specification may be changed.
    dayOffset = 120

    # Japanese company often submits the securities report on June.
    # currentTime = datetime.datetime.now() - datetime.timedelta(days = 150)
    currentTime = datetime.datetime.now()

    # Matching disclosure list.
    disclosureList = []

    # constructor is not existed.
    # def __init__(self):


    # require: Stock code
    # return: [] {secCode, filerName, docId, docDescription}

    # secCode: The stock code.
    # filerName: A submitter. This name is often a company name.
    # docId: The disclosure number managed by EDINET.
    # docDescription: Title of disclosure.
    def searchDis (self, stockCode):
        # while example. This spec wad abolished.
        # while currentTime.date() > datetime.date(2021, 10, 30):
        dci = dsi.disclosureInspection()
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
                if (jsonData["results"][num]["secCode"] == stockCode and
                    dci.isDisclosureOfCorporateInformation(jsonData["results"][num]["ordinanceCode"]) and
                    (dci.isSecuritiesReportCode(jsonData["results"][num]["formCode"]) or 
                        dci.isQuarterlyReport(jsonData["results"][num]["formCode"])
                    ) and
                    dci.isListedCompany(jsonData["results"][num]["secCode"])
                ):
                    self.disclosureList.append({
                        "formCode": jsonData["results"][num]["formCode"],
                        "submitDateTime": jsonData["results"][num]["submitDateTime"][:10],
                        "periodEnd": jsonData["results"][num]["periodEnd"],
                        "edinetCode": jsonData["results"][num]["edinetCode"],
                        "secCode": jsonData["results"][num]["secCode"],
                        "filerName": jsonData["results"][num]["filerName"],
                        "docID": jsonData["results"][num]["docID"],
                        "docDescription": jsonData["results"][num]["docDescription"]
                    })
                    # pprint.pprint (jsonData["results"][num])
                    break
            if (len(self.disclosureList)): break
        return self.disclosureList

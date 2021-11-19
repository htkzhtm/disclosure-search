import pprint
import sys
from disclosureModule import searchDisclosure as sdc
from disclosureModule import acquireDisclosure as daq
from disclosureModule import stockCodeGuarantee as scg

searcher = sdc.disSearcher()
acquirer = daq.disAcquirer()
stockCG = scg.stockCodeClass()

if len(sys.argv) < 2 or (not stockCG.isStockCode(sys.argv[1])):
    print('Stock code is illegal. Check it')
    exit()

# check the disclosure existing or not. Requires pprint pack.
disclosureDetails = searcher.searchDis()

if len(disclosureDetails) == 0:
    print('Disclosure does not exist')
    exit()
pprint.pprint (disclosureDetails)

# Download the PDF and Zip
for delta in range(0, len(disclosureDetails)):
    acquirer.aqquireDisclosurePDF(disclosureDetails[delta]["docID"])
    acquirer.aqquireDisclosureZip(disclosureDetails[delta]["docID"])

    # Write Binary is too long. This commentout is for debug
    # exit()

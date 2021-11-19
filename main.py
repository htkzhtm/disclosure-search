import pprint
from disclosureModule import searchDisclosure as sdc
from disclosureModule import acquireDisclosure as daq

searcher = sdc.disSearcher()
acquirer = daq.disAcquirer()

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

import pprint
from disclusureModule import searchDisclosure as sdc
from disclusureModule import acquireDisclosure as daq

searcher = sdc.disSearcher()
acquirer = daq.disAcquirer()

# check the disclosure existing or not. Requires pprint pack.
disclosureDetails = searcher.searchDis()

if len(disclosureDetails) == 0:
    print('Disclosure does not exist')
    exit()
pprint.pprint (disclosureDetails)

# Download the PDF
acquirer.aqquireDisclosurePDF(disclosureDetails[0]["docID"])

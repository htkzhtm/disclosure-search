import pprint
import sys
from src.disclosureModule import searchDisclosure as sdc
from src.disclosureModule import acquireDisclosure as daq
from src.disclosureModule import stockCodeGuarantee as scg
from src.disclosureModule import unzipDisclosure as uzd
from src.wordCloudModule import wordCloudGenerator as wcg

searcher = sdc.disSearcher()
acquirer = daq.disAcquirer()
stockCG = scg.stockCodeClass()
unzipper = uzd.zipDisclosure()
wc = wcg.wordClouder()

if len(sys.argv) < 2 or (not stockCG.isStockCode(sys.argv[1])):
    print('Stock code is illegal. Check it')
    exit()

disclosureDetails = searcher.searchDis(stockCG.genarateStockCode(sys.argv[1]))

if not len(disclosureDetails):
    print('Disclosure does not exist')
    exit()
# check the disclosure existing or not. Requires pprint pack.
pprint.pprint (disclosureDetails)

for delta in range(0, len(disclosureDetails)):
    # Download the PDF and Zip
    acquirer.aqquireDisclosurePDF(disclosureDetails[delta]["docID"])
    acquirer.aqquireDisclosureZip(disclosureDetails[delta]["docID"])

    # Unzip
    unzipper.unzipDisclosure(disclosureDetails[delta]["docID"])

    # Write Binary is too long. This commentout is for debug
    # exit()
    # wordCloud generation.
    wc.generateWordCloud(
        disclosureDetails[delta]["edinetCode"],
        disclosureDetails[delta]["periodEnd"],
        disclosureDetails[delta]["submitDateTime"],
        disclosureDetails[delta]["formCode"]
    )

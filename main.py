import pprint
from disclusureModule import searchDisclosure as sdc

ob = sdc.disSearcher()

# check the disclosure existing or not. Requires pprint pack.
pprint.pprint (ob.searchDis())

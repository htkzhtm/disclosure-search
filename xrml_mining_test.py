import re
from lxml import etree

filename = "./XBRL/PublicDoc/jpcrp040300-q2r-001_E07801-000_2021-09-30_01_2021-11-15.xbrl"

head = etree.parse(filename).getroot()

company = head.find("jpcrp_cor:CompanyNameCoverPage",head.nsmap).text
description = head.find("jpcrp_cor:DescriptionOfBusinessTextBlock",head.nsmap).text
description = re.sub('\s','',description)
description = re.sub('<.*?>','',description)

print(description)



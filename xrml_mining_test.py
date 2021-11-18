import re
from lxml import etree
from janome.tokenizer import Tokenizer

filename = "./XBRL/PublicDoc/jpcrp040300-q2r-001_E07801-000_2021-09-30_01_2021-11-15.xbrl"

head = etree.parse(filename).getroot()

company = head.find("jpcrp_cor:CompanyNameCoverPage",head.nsmap).text
description = head.find("jpcrp_cor:DescriptionOfBusinessTextBlock",head.nsmap).text
description = re.sub('\s','',description)
description = re.sub('<.*?>','',description)

print(description)

t = Tokenizer()
words = []
for token in t.tokenize(description):
    if token.part_of_speech.split(',')[0] in ['形容詞', '動詞', '名詞']:
        words.append(token.base_form)

print(words)
    
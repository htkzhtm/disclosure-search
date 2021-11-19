import re
from lxml import etree
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud

filename = "./XBRL/PublicDoc/jpcrp030000-asr-001_E02367-000_2021-03-31_01_2021-06-30.xbrl"

head = etree.parse(filename).getroot()

company = head.find("jpcrp_cor:CompanyNameCoverPage",head.nsmap).text
description = head.find("jpcrp_cor:BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock",head.nsmap).text
description = re.sub('\s','',description)
description = re.sub('<.*?>','',description)

#print(description)

t = Tokenizer()
words = []
for token in t.tokenize(description):
    if token.part_of_speech.split(',')[0] in ['形容詞', '動詞', '名詞']:
        words.append(token.base_form)

#print(words)

wordcloud = WordCloud(
    background_color='white', 
    font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W2.ttc', 
    stopwords = ['株式会社', '当社', '事業','関連','内容','セグメント','とおり', '現在', '会社','関係']
)
wordcloud.generate(' '.join(words))
wordcloud.to_file('wordcloud.png')

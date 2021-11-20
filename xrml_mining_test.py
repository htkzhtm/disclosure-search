import re
from lxml import etree
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud

# Nintendo
filename = "./XBRL/PublicDoc/jpcrp030000-asr-001_E02367-000_2021-03-31_01_2021-06-30.xbrl"

head = etree.parse(filename).getroot()

company = head.find("jpcrp_cor:CompanyNameCoverPage",head.nsmap).text
description = head.find("jpcrp_cor:BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock",head.nsmap).text
description = re.sub('¥s','',description)
description = re.sub('<.*?>','',description)

print(description)

t = Tokenizer()
words = []
for token in t.tokenize(description):
    if token.part_of_speech.split(',')[0] in ['形容詞', '動詞', '名詞']:
        words.append(token.base_form)

#print(words)

wordcloud = WordCloud(
    background_color='white', 
    font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W2.ttc', 
    stopwords = [
        '株式会社', '当社', '事業','関連','内容','セグメント', '品', '事項', '上', '性', '視点', '次', '人', '時',
        '文中', 'とおり', '現在', '会社','関係', '会計', '等', '業界', 'ビジネス', '的', '末', '対処', '人々',
        '用', '状況', '下', '取り組み', '確立', 'グループ', '社員', '前年', '同期', '前年同期', '当期',
        '力', '連結', '年度', '我々', '要因', '化', '千', '円', '社会', '日本', '市場', '企業', '年', '月', '取締役',
        'クライアント', '可能', '委員', '活動', '足', '自己', '率', '期', '皆様', '基本', '主', '以下', '目安', '認識',
        '代表', 'コーポレート', 'ガバナンス', '高', '浸透', '点', '総合', '以上', 'モデル', '万', '億', '兆', '分野', 'クラス',
        'ランキング', '理念', 'カンパニー', '会', '経営', '目標', '計画', '設定', '短期', '中期', '長期',
        '思う', '持つ', 'しまう', 'いただける', '行える', '取り巻く', 'まいる', 'おる', 'できる', '向ける',
        '取り組む', '図る', 'いたす', '含める', '受ける', '行う', 'おこなう', '基づく', '考える', 'おきる', '応じる',
        '示す', '含む',
        'もつ', '新た', '確か', 'たち',
        'する', 'いる', 'こと', 'よう', 'いく', 'ある', 'ため', 'せる', 'くる', 'いただく', 'ない', 'さ', 
        'いい', 'くれる', 'こと', 'これ', 'さん', 'せる', 'そう', 'てる',  'なる', 'の', 'もてる',
        'みたい', 'やる', 'よい', 'よう', 'られる', 'れる', 'ん', 'もと', 'どなた', 'これら', 'もの', 'つく'
    ]
)
wordcloud.generate(' '.join(words))
wordcloud.to_file('wordcloud.png')

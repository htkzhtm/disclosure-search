# check 32 page https://www.fsa.go.jp/search/20191101/2b-1_InstanceGuide.pdf
# wordCloud generator used by xbrl.

import os
import re
from ..disclosureSpecification import inspection as dsi
from . import wordCloudConfig as wcc
from lxml import etree
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud

#notes.
#str = "jpcrp" + "{有報は030000, 四半期は043000}" + "-" + "{asr, q3r, q2r q1r のどれか}" + "-" + "001_" + edinetCode + "-000_" + periodEnd + "_01_" + submitDateTime + ".xbrl"

class wordClouder:

    baseName = "jpcrp"

    # Generate. This Spec will be modified.
    def generateWordCloud (self, edinetCode, periodEnd, submitDateTime, formCode):
        conf = wcc.configClass()
        fileNamePattern = self.generateXbrlFileNamePattern(edinetCode, periodEnd, submitDateTime, formCode)
        baseFilePath = conf.tosXbrlLBasePath()
        description = None

        # check the File Existing. If it exists, generate the word cloud.
        for delta in range(0, len(fileNamePattern)):
            filePath = baseFilePath + fileNamePattern[delta]
            if os.path.isfile(filePath):
                description = self.generateXbrlDescription(filePath, formCode)
        
        if not description:
            print("File is missing. Check your debug. Generated File Pattern is following")
            print(fileNamePattern)

        # Janome analysis.
        t = Tokenizer()
        words = []
        for token in t.tokenize(description):
            if token.part_of_speech.split(',')[0] in ['形容詞', '動詞', '名詞']:
                words.append(token.base_form)

        wordcloud = WordCloud(
            background_color = conf.backgroundColor,
            font_path = conf.fontPath,
            stopwords = conf.stopWordsArray,
        )
        wordcloud.generate(' '.join(words))
        wordcloud.to_file(conf.tosWordCloudPath() + 'wordcloud.png')


    # Return the ARRAY datatype.
    # Quarterly report cannnot be identified even if API response is used.
    def generateXbrlFileNamePattern (self, edinetCode, periodEnd, submitDateTime, formCode):
        dci = dsi.disclosureInspection()
        if dci.isSecuritiesReportCode(formCode):
            forwardNamePart = self.baseName + formCode + "-"
        else: 
            forwardNamePart = self.baseName + dci.tosQuarterlyReportCodeForXbrl(formCode) + "-"
        BackwardNamePart = "-001_" + edinetCode + "-000_" + periodEnd + "_01_" + submitDateTime + ".xbrl"
        if dci.isSecuritiesReportCode(formCode):
            return [forwardNamePart + "asr" + BackwardNamePart]
        else:
            return [
                forwardNamePart + "q3r" + BackwardNamePart,
                forwardNamePart + "q2r" + BackwardNamePart,
                forwardNamePart + "q1r" + BackwardNamePart,
            ]

    # return the description of disclosure.
    def generateXbrlDescription (self, filePath, formCode):
        dci = dsi.disclosureInspection()
        head = etree.parse(filePath).getroot()
        
        # For example, company name is following.
        # company = head.find("jpcrp_cor:CompanyNameCoverPage",head.nsmap).text

        # Get the description.
        # Xbrl Spec is here("タクソノミ要素リスト") https://disclosure.edinet-fsa.go.jp/EKW0EZ0015.html
        description = head.find(dci.tosBusinessContentTakusonomi(), head.nsmap).text
        description = re.sub('¥s','',description)
        description = re.sub('<.*?>','',description)

        # Quarterly Report cannnot use.
        if dci.isSecuritiesReportCode(formCode):
            Issue = head.find(dci.tosBusPolEnvIssuesTakusonomi(), head.nsmap).text
            Issue = re.sub('¥s','',Issue)
            Issue = re.sub('<.*?>','',Issue)
            description += Issue

        # print (description)
        return description

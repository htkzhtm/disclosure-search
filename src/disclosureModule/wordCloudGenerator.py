# check 32 page https://www.fsa.go.jp/search/20191101/2b-1_InstanceGuide.pdf
# Disclosure zip file.

import os

class wordClouder:
    def generateWordCloud (self, edinetCode, periodEnd, submitDateTime):
        str = "jpcrp" + "{有報は030000, 四半期は043000}" + "-" + "{asr, q3r, q2r q1r のどれか}" + "-" + "001_" + edinetCode + "-000_" + periodEnd + "_01_" + submitDateTime + ".xbrl"
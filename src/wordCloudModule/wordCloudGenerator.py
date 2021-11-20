# check 32 page https://www.fsa.go.jp/search/20191101/2b-1_InstanceGuide.pdf
# wordCloud generator used by xbrl.

import os
from ..disclosureSpecification import inspection as dsi

#notes.
#str = "jpcrp" + "{有報は030000, 四半期は043000}" + "-" + "{asr, q3r, q2r q1r のどれか}" + "-" + "001_" + edinetCode + "-000_" + periodEnd + "_01_" + submitDateTime + ".xbrl"

class wordClouder:

    baseName = "jpcrp"

    # Return the ARRAY datatype.
    # Quarterly report cannnot be identified even if API response is used.
    def generateXbrlFileNamePattern (self, edinetCode, periodEnd, submitDateTime, formCode):
        dci = dsi.disclosureInspection()
        forwardNamePart = self.baseName + formCode + "-"
        BackwardNamePart = "-001_" + edinetCode + "-000_" + periodEnd + "_01_" + submitDateTime + ".xbrl"
        if formCode == dci.isSecuritiesReportCode:
            return [forwardNamePart + "asr" + BackwardNamePart]
        else:
            return [
                forwardNamePart + "q3r" + BackwardNamePart,
                forwardNamePart + "q2r" + BackwardNamePart,
                forwardNamePart + "q1r" + BackwardNamePart,
            ]

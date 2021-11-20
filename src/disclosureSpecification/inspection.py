class disclosureInspection:

    # formCode
    # 030000: Securities report
    # 043000: Quarterly Report
    SecuritiesReportCode = "030000"
    QuarterlyReportCode = "043000"

    # ordinanceCode
    # 010: Cabinet Office Ordinance on Disclosure of Corporate Information, etc.
    DisclosureOfCorporateInform = "010"

    # requires: string
    # return: boolean
    def isSecuritiesReportCode (self, formCode):
        return formCode == self.SecuritiesReportCode

    def isQuarterlyReport (self, formCode):
        return formCode == self.QuarterlyReportCode

    def isDisclosureOfCorporateInformation (self, ordinanceCode): 
        return ordinanceCode == self.DisclosureOfCorporateInform

    # This function maybe NOT need.
    def isListedCompany (self, secCode):
        return secCode != None

    # FormCode of Quarterly Report for xbrl is into 040 "3" 00
    def tosQuarterlyReportCodeForXbrl (self, secCode):
        return "040300" if secCode == self.QuarterlyReportCode else secCode

    # Function Name.
    def tosBusinessContentTakusonomi (self):
        return "jpcrp_cor:DescriptionOfBusinessTextBlock"

    # Management policy, business environment, issues to be dealt with, etc.
    # This element CANNOT use in case DISCLOSURE is QUAETERLY REPORT.
    def tosBusPolEnvIssuesTakusonomi (self):
        return "jpcrp_cor:BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock"

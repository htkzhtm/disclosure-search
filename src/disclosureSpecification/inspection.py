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

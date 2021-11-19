# Stock Code Class

class stockCodeClass:

    # Validation for stock code.
    # require: stockCode: string
    # return: boolean
    def isStockCode (self, stockCode):
        return (
            stockCode.isdigit() and
            len(stockCode) == 4 and
            int(stockCode) > 1000 and
            int(stockCode) < 9999
        )

    # stock code generation for disclosure search.
    # require: stockCode: string
    # return: string
    def genarateStockCode (self, stockCode):
        return stockCode + "0"
        
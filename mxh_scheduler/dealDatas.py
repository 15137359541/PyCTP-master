# 对CTP返回的dict结构内部的元素编码从bytes转换为utf-8，该方法也适用于单个变量的格式转换
def code_transform(data):
    # 传入参数为list
    if isinstance(data, list):
        list_output = []
        for i_dict in data:
            if isinstance(i_dict, dict):  # k是个dict
                data_output = {}
                for j_key in i_dict:  # j是dict内部单个元素的key
                    data_output[j_key] = code_transform(i_dict[j_key])
                list_output.append(data_output)
        return list_output
    # 传入参数为dict
    elif isinstance(data, dict):
        data_output = {}
        for i in data:
            data_output[i] = code_transform(data[i])
        return data_output
    # 传入参数为单个变量
    elif isinstance(data, bytes):
        return data.decode('gbk')
    else:
        return data
# def seleceDatas(data):


if __name__ =='__main__':
    con = {'AskPrice3': 1.7976931348623157e+308, 'OpenInterest': 325016.0, 'AskPrice1': 2510.5, 'UpdateTime': '07:54:41', 'BidVolume2': 0, 'ExchangeID': 'DCE', 'BidVolume1': 4, 'BidPrice3': 1.7976931348623157e+308, 'AskPrice5': 1.7976931348623157e+308, 'BidPrice1': 2509.5, 'BidVolume4': 0, 'AskVolume3': 0, 'PreDelta': 0.0, 'LowestPrice': 2476.5, 'Volume': 329376, 'AskVolume1': 88, 'AskPrice4': 1.7976931348623157e+308, 'InstrumentID': 'j1901', 'PreClosePrice': 2504.5, 'ExchangeInstID': 'j1901', 'LastPrice': 2510.0, 'UpdateMillisec': 500, 'HighestPrice': 2525.5, 'AskPrice2': 1.7976931348623157e+308, 'SettlementPrice': 1.7976931348623157e+308, 'BidPrice4': 1.7976931348623157e+308, 'LowerLimitPrice': 2351.0, 'Turnover': 82445048200.0, 'UpperLimitPrice': 2759.0, 'AskVolume5': 0, 'BidPrice2': 1.7976931348623157e+308, 'OpenPrice': 2508.0, 'AskVolume4': 0, 'BidVolume3': 0, 'PreOpenInterest': 372030.0, 'AskVolume2': 0, 'CurrDelta': 1.7976931348623157e+308, 'ActionDay': '20180824', 'BidVolume5': 0, 'BidPrice5': 1.7976931348623157e+308, 'AveragePrice': 250306.78677256388, 'ClosePrice': 1.7976931348623157e+308, 'TradingDay': '20180824', 'PreSettlementPrice': 2555.0}
    res = code_transform(con)
    print(type(res),'内容是：',res)
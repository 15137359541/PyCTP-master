import datetime
# 对CTP_API返回的dict结构内部的元素编码从bytes转换为utf-8，该方法也适用于单个变量的格式转换
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
#传过来的数据是上面函数的结果列表
def put_Mongo(data):
    data_output = {}
    for item in data:
        data_output["UpdateTime"] = item.get("UpdateTime")
        data_output['ActionDay'] = item.get('ActionDay')
        data_output['LastPrice'] = item.get('LastPrice')
        data_output["datetime"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data_output

if __name__=="__main__":
    data = {'AskVolume1': 88, 'AskVolume5': 0, 'BidPrice5': 1.7976931348623157e+308, 'UpperLimitPrice': 2759.0, 'LowestPrice': 2476.5, 'BidVolume5': 0, 'AskPrice4': 1.7976931348623157e+308, 'AskVolume4': 0, 'AskVolume3': 0, 'CurrDelta': 1.7976931348623157e+308, 'OpenInterest': 325016.0, 'AveragePrice': 250306.78677256388, 'PreDelta': 0.0, 'TradingDay': '20180824', 'SettlementPrice': 1.7976931348623157e+308, 'InstrumentID': 'j1901', 'BidVolume4': 0, 'AskPrice5': 1.7976931348623157e+308, 'ActionDay': '20180824', 'LowerLimitPrice': 2351.0, 'ClosePrice': 1.7976931348623157e+308, 'BidVolume2': 0, 'BidPrice3': 1.7976931348623157e+308, 'AskPrice3': 1.7976931348623157e+308, 'BidPrice1': 2509.5, 'ExchangeInstID': 'j1901', 'UpdateTime': '07:54:41', 'ExchangeID': 'DCE', 'HighestPrice': 2525.5, 'UpdateMillisec': 500, 'Turnover': 82445048200.0, 'LastPrice': 2510.0, 'AskPrice2': 1.7976931348623157e+308, 'BidVolume1': 4, 'AskVolume2': 0, 'OpenPrice': 2508.0, 'AskPrice1': 2510.5, 'Volume': 329376, 'BidPrice4': 1.7976931348623157e+308, 'PreClosePrice': 2504.5, 'BidPrice2': 1.7976931348623157e+308, 'PreOpenInterest': 372030.0, 'BidVolume3': 0, 'PreSettlementPrice': 2555.0}
    date1=[{'CurrDelta': 1.7976931348623157e+308, 'OpenPrice': 2450.5, 'AskPrice5': 1.7976931348623157e+308, 'BidVolume4': 0, 'ExchangeID': 'DCE', 'ClosePrice': 1.7976931348623157e+308, 'UpperLimitPrice': 2678.0, 'InstrumentID': 'j1901', 'OpenInterest': 357216.0, 'AskVolume4': 0, 'AskVolume1': 9, 'BidVolume2': 0, 'BidVolume5': 0, 'PreDelta': 0.0, 'AveragePrice': 243504.21446248895, 'ExchangeInstID': 'j1901', 'BidPrice4': 1.7976931348623157e+308, 'AskVolume2': 0, 'LowerLimitPrice': 2328.0, 'PreOpenInterest': 413152.0, 'LowestPrice': 2404.0, 'BidPrice1': 2444.0, 'HighestPrice': 2468.0, 'AskPrice4': 1.7976931348623157e+308, 'UpdateTime': '13:39:31', 'TradingDay': '20180831', 'AskVolume5': 0, 'AskPrice1': 2444.5, 'BidPrice3': 1.7976931348623157e+308, 'AskPrice2': 1.7976931348623157e+308, 'ActionDay': '20180831', 'Volume': 553570, 'AskVolume3': 0, 'PreClosePrice': 2448.0, 'BidPrice5': 1.7976931348623157e+308, 'BidVolume1': 11, 'BidVolume3': 0, 'UpdateMillisec': 500, 'LastPrice': 2444.0, 'SettlementPrice': 1.7976931348623157e+308, 'PreSettlementPrice': 2503.0, 'Turnover': 134796628000.0, 'AskPrice3': 1.7976931348623157e+308, 'BidPrice2': 1.7976931348623157e+308}]

    res = code_transform(put_Mongo(date1))
    print(res)



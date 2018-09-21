import json
new_dict = {"future code":"j1901"}
# with open("Futures_.json","w") as f:
#     json.dump(new_dict,f)
#     print("加载入文件完成...")

with open('Futures_.json','r',encoding='utf-8') as json_file:
    model = json.load(json_file)
print(model['future code'])
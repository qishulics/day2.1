import yaml

# with open("./data.yml") as f:
#     data = yaml.load(f)
#     print(data.get("Test"))
#     # print(type(data.get("YML_Data")))
#     # print(data.get("da2"))
#     # print(data.get("login_data01"))
#
#
#     # dic = data.get("Test")
#     # print(dic)
#     # for key in dic.keys():
#     #     print(key)

data = {'login_data02': {'pwd': 567, 'se': 'nan', 'name': 'nana'}, 'login_data01': {'pwd': 456, 'name': 'lili'}, 'sex': {'se': '男'}}

with open("./data.yml","w") as f:
    w_data = yaml.dump(data,f)
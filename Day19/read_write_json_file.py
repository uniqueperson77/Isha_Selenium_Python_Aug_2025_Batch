import json
from jsonpath_ng import parse
from Common_Functions import generic_functions as gf

filepath=r"D:\Isha\SeleniumPythonClass\Day19\Results\get_response.json"
data = gf.read_data(filepath)
json_dict = json.loads(data)


#retrive or update data on this json req/response
print(json_dict)
obj = parse("$.key3.base[0].base2")
obj.update(json_dict,850)
print(json_dict)


f = open(filepath,"w")
json.dump(json_dict,f)
f.close()


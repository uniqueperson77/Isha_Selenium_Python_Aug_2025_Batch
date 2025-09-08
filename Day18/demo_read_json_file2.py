import json
fp = r"D:\Isha\SeleniumPythonClass\External_files\sample.json"        #  \t  \n
f = open(fp,"r")

obj = json.load(f)
print(obj)
print(type(obj))

f.close()

# print(obj['response']['country'])
list_of_records = obj['response']
print(type(list_of_records))
print(list_of_records[0]['wickets_taken'])
print(list_of_records[1]['wickets_taken'])


obj = {"key1":"value1","key2":[2,5,10],"key3":{"base":[{"base1":1,"base2":2},{"base3":3,"base4":4}]}}

print(obj["key2"][1])

print(obj["key3"]["base"][0]["base2"])

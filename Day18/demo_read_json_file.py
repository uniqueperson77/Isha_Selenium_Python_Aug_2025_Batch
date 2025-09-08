# pre req json module/package
import json
# import time

fp = r"D:\Isha\SeleniumPythonClass\External_files\sample.json"        #  \t  \n
f = open(fp,"r")
data = f.read()
f.close()

# print(data)
# print(type(data))

obj = json.loads(data)
print(obj)
print(type(obj))

record = obj['response']
print(record)
print(record['name'])

print(obj['response']['name'])

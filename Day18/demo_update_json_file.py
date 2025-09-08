import json

json_data= {"key":1000}

fp = r"D:\Isha\SeleniumPythonClass\External_files\sample3.json"        #  \t  \n
f = open(fp,"w")

json.dump(json_data,f)


f.close()
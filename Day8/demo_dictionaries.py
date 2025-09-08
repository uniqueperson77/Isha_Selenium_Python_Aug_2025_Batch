# d={}
# d1= dict()
# print(d,d1,type(d),type(d1))

# with in dict every key value pair will separated by , & key:value
d = {"Isha":"9559550000"}
d1 = {1:100}
d2 = {1.5:100}
d3 = {True:"Correct"}


d4 = {1:100,2:200,"Isha":9000,"INDIA":["AP","Gujarat","TN","Kerala"]}


# print(d4.keys())
# # print(type(d4.keys()))
# keys = d4.keys()
# # print(keys[0])        # no direct access through index
# print(d4.values())
# print(d4.items())
#
# print(d4.get("INDIA"))
# print(d4["INDIA"])
#
# print(d4)
# # d4[2] = "UPDATE"
# d4.update({2:"NEW"})
# print(d4)

# print(d4.get("INDIAA"))
# print(d4["INDIAA"])

# d4.pop('Isha')
# print(d4)



# for item in d4.items():
#     print (item)
#
# for key,value in d4.items():
#     print(key,value)

for key in d4.keys():       #key INDIA was present
    if "INDIA-B" == key:
        print("Key was present")



d5 = {"INDIA":{"TN":"Chennai","AP":"Amaravthi","TNG":"Hyderabad"}}
print(d5)
print(d5.get("INDIA").get("AP"))
print(d5["INDIA"]["TN"])

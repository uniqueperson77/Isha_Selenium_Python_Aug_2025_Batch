# data types
    #Numeric - int, float, complex  (2+3j)
    #Sequential - string, list & tuple



def sample_string():
    name= "            isha is very good person       "       # 4 characters  0,1,2,3
    print(name)
    name = name.strip()
    print(name)
    exit()
    index_for_h = name.index("i")
    print(index_for_h)
    name1 = name.upper()
    print(name1)
    name2 = name.lower()
    print(name2)
    name3 = name.capitalize()
    print(name3)
    count_of_char = name.count("is")
    print(count_of_char)

    var = "5000"
    print(var.isdigit())

# sample_string()


# for i in range(1,501):      #1,...99,100
#     print(i)
#     if i==200:
#         break


# list contains objects (string, list, integers,float, boolean,...)
#list should enclose with [] and every object within list is separated by comma

l1 = [2,3,4,5]
l2 = [1.5,5.7,2.3,3.4,"Is","Are"]
l3 = ["Isha","Sachin","Dhoni","Virat",True,False]
# print(type(l2))
print(len(l3))

# print(l1[2])
# print(l3[5])
# print(l3[:10])      #0,1,..9

print(l3[2:])      #2,3      #list_variable[start_index:stop_index]
# print(l2[2])








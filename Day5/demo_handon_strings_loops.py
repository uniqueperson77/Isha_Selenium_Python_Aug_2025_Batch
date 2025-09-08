s= "Hello World"
# print(s[1])

char = "o"
length_of_string = len(s)
# length_of_string = 11

for i in range(0,length_of_string):       #0,1,2,3,4,5,6,....10
    act_val = s[i]
    if act_val == char:
        print(i)
        break
    # print(act_val)
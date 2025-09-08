sample = "     Hello World       "

s1=""
for value in sample:        #iterating through element or value  #    H,e,l,l,o, ,
    # if value == " ":
    #     pass
    # else:
    #     s1=s1+value

    if value !=" ":
        s1 = s1 + value


for index in range(0,len(sample)):        #0,1,2,3...9
    print(sample[index])
    pass

print(s1)








exit()
sample2 =sample.strip()
print(sample)
print(sample2)
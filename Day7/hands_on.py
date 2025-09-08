# sample = "     Hello World       "
# sample = "Hello World       "
# sample = "    Hello     World"
sample = "    Hello  World"
s=""

def check_presence_of_char(ss):
    flag = False
    for char in ss:
        if ord(char) !=32:
            flag = True
            break
    return flag


for i in range(0, len(sample)):
    if sample[i] == " ":
        try:
            if check_presence_of_char(sample[0:i]) and check_presence_of_char(sample[i+1:]) :
                s=s+sample[i]
        except:
            pass
    else:
        s = s + sample[i]




print(s)
# print(sample.strip())
exit()

# print(ord(" "))
# chr()

# for i in range(0, len(sample)):
#     if sample[i] == " ":
#         try:
#             if sample[i+1] != " " and sample[i-1] != " ":
#                 s=s+sample[i]
#         except:
#             pass
#     else:
#         s = s + sample[i]



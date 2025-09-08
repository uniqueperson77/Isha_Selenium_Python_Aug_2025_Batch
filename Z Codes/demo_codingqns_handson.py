# l=[2,4,10,8,6,6,8,10,'Isha','ISHA','Isha']
# s = set(l)          # remove the duplicates
# l2 = list(s)
# print(l2)


# new_list =[]
#
# for i in l:
#     if i not in new_list:
#         new_list.append(i)
#
#
# print(new_list)

l=[2,4,10,8,6,6,8,10,255,122,10]
l2 = list(set(l))
l2.sort()
print(l2)

# print(l2[len(l2)-1])
print(l2[-1])
print(l2[-2])
print(l2[0])
# l.sort()
# print(l)



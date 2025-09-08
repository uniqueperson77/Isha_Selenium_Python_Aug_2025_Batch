#program to sum of first five even numbers using while loop
# 2 4 6 8 10
sum=0
n=10
i=2
while i <=n*2:        #i=2,3
    sum = sum+i
    i=i+2
print("sum of even numbers : " + str(sum))

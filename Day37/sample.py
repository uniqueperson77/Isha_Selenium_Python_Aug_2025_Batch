
s= 1+ 1
s1= "1"+"1"
print(s,s1)
try:
    # s2 = 1 + "1"
    s3 = 1/0
except Exception as e:
    print(e)
    assert False
finally:
    pass


print(s3)

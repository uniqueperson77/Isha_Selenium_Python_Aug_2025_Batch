def add(*args):
    # res=0
    # for value in args:
    #     res = res+value
    # print(res)
    res = sum(args)
    print(res)

def add2(**kwargs):
    res=0
    for var in kwargs.values():
        res = res+var
    print(res)
    return res



#a,b,c,d,e,...

# add(2,4,6,8,10,12)
# result = add2(a=2,b=5,c=10,d=100)
# print(result)

def func1(a=10,b=10):
    print(a,b)

func1(300,500)
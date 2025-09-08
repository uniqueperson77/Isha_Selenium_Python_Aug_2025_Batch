import os

def file_write():
    f = open("file2.txt","w")       # creating a file if it was not present & erase the content in file
    f.write("Hello World")
    f.close()
    f = open("file2.txt","a")   # this mode will not erase the content in existing file
    f.write("\nHi Hello")
    f.close()

def file_read():
    exp_file=open("exp.txt","r")
    # data = exp_file.read()
    # print(data)
    # print(type(data))
    list_of_lines = exp_file.readlines()
    print(list_of_lines)
    print(list_of_lines[1])
    exp_file.close()


def file_write1():
    # f = open(r"D:\Isha\SeleniumPythonClass\External_files\file5.txt","w")
    # f.close()
    with open(r"D:\Isha\SeleniumPythonClass\External_files\file5.txt","w") as f:
        f.write("ncsnjcn")


file_read()
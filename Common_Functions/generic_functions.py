def write_data_to_file(fp,content):
    obj = open(fp, "w")
    obj.write(content)
    obj.close()

def read_data(fp):
    obj = open(fp, "r")
    data = obj.read()
    obj.close()
    return data
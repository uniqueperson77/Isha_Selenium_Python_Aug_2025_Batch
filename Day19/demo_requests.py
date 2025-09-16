import requests
from Common_Functions import generic_functions as gf

#steps1: requests, python,get endpoint,


username = "admin"
password = "admin"

def rest_get():
    end_point_url = "http://127.0.0.1:8000/api/bowlers/"
    response_obj = requests.get(end_point_url,auth=(username,password))
    # print(type(response_obj))
    print(response_obj)
    print(response_obj.text)
    print(response_obj.status_code)


    # logging the evidence in static files
    filepath=r"D:\Isha\SeleniumPythonClass\Day19\Results\get_response.json"
    gf.write_data_to_file(filepath,response_obj.text)

def rest_post():
    url = "http://127.0.0.1:8000/api/bowlers/"
    req={"name": "Ronaldo",
        "age": 40,
        "country": "INDIA",
        "wickets_taken": 500,
        "bowling_average": 100.0,
        "bowling_strikerate": 50.0,
        "economy_rate": 1.33}
    obj = requests.post(url,json=req,auth=(username,password))
    print(obj.status_code)
    print(obj.text)



# rest_post()
# rest_get()
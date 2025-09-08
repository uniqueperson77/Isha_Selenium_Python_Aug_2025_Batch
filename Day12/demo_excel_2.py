import pyodbc
# list_of_drivers = pyodbc.drivers()
# # print(list_of_drivers)
# for driver in list_of_drivers:
#     print(driver)


# str1 = "Isha"
# str2 = "Class"
# str21 = "Finished"
# str3 = "IshaClass"
# str4 = "Isha" + str2 + "Finished"
# print(str4)

# exit()

db_path = r"D:\Isha\SeleniumPythonClass\External_files\TestData.xlsx"
driver = "Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)"
connection_string = "Driver={"+driver+"};DBQ="+db_path+";ReadOnly=True"
print(connection_string)

conn = pyodbc.connect(connection_string,autocommit=True)
print("Connection established")
cursor_obj = conn.cursor()

#Reading
# query="SELECT * from [Data$]"
# cursor_obj.execute(query)
# records = cursor_obj.fetchall()
# print(records)

#updating
# sql_query = "update [Data$] set Username='new_suresh' where S_No='TC_2'"
# cursor_obj.execute(sql_query)

#create
query = "insert into [Data$] values('TC_8','random','369','yes')"
cursor_obj.execute(query)

#delete (not supported)
# cursor_obj.execute("delete from [Data$] where Username='Virat'")



cursor_obj.close()
conn.close()
print("Connection closed")





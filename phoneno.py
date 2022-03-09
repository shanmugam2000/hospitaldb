import sqlite3
data = sqlite3.connect("hospital.db")
getDocphno = input("enter the doctor phone number to be searched:")
result = data.execute("select * from doctordata where docphno="+getDocphno)
for i in result:
        print("docname",i[2])
        print("docqualification",i[3])
        print("docphno",i[5])
        print("docemail",i[4])
        print("docemail",i[5])
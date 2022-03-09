import sqlite3
data = sqlite3.connect("hospital.db")
getDocphno = input("Enter doctor phone number to be deleted")
data.execute("delete from doctordata where docphno="+getDocphno)
data.commit()
print("deleted succesfully")

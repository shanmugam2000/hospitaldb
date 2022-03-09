import sqlite3
data = sqlite3.connect("hospital.db")
getId = input("Enter patient id to be deleted")
data.execute("delete from patient where id="+getId)
data.commit()
print("deleted succesfully")

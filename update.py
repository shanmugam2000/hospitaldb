import sqlite3
data = sqlite3.connect("hospital.db")
getId = input("Enter patient Id to be updated: ")
getPatName = input("Enter new patient Name: ")
getPatAddress = input("Enter new patient address: ")
getPatPhno = input("Enter new patient phone number: ")
getPatEmail = input("Enter new patient email: ")
getPatPincode = input("Enter new patient pincode: ")
data.execute("update patient set patname='"+getPatName+"',pataddress='"+getPatAddress+"',patphno="+getPatPhno+",\
             patemail='"+getPatEmail+"',patpincode="+getPatPincode+" where id="+getId)

data.commit()
print("updated succesfully")
result = data.execute("select * from patient")
for i in result:
      print("patient id", i[0])
      print("patient name", i[2])
      print("patient address", i[3])
      print("patient phno", i[5])
      print("patient email", i[4])
      print("patient pincode", i[5])



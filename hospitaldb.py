import sqlite3
patientdata = sqlite3.connect("hospital.db")
patientdata.execute(''' create table patient(
                      id integer primary key autoincrement,
                      patname text,
                      pataddress text,
                      patphno integer,
                      patemail text,
                      patpincode integer

);  ''')

getId = input("Enter patient Id: ")
getPatName = input("Enter patient Name: ")
getPatAddress = input("Enter patient address: ")
getPatPhno = input("Enter patient phone number: ")
getPatEmail = input("Enter patient email: ")
getPatPincode = input("Enter patient pincode: ")
patientdata.execute("insert into patient(id,patname,pataddress,patphno,patemail,patpincode) \
values("+getId+",'"+getPatName+"','"+getPatAddress+"',"+getPatPhno+",'"+getPatEmail+"',"+getPatPincode+")")
patientdata.commit()
patientdata.close()
doctor = sqlite3.connect("hospital.db")
doctor.execute('''create table doctordata(
                      docname text,
                      docqualification text,
                      docaddress text,
                      docphno integer,
                      docemail text
               
);  ''')
getDocname = input("Enter doctor name: ")
getDocqualification = input("Enter doctor qualification: ")
getDocaddress = input("Enter doctor address: ")
getDocphno = input("Enter doctor phone number: ")
getDocemail = input("Enter doctor email: ")
doctor.execute("insert into doctordata(docname,docqualification,docaddress,docphno,docemail) \
    values('"+getDocname+"','"+getDocqualification+"','"+getDocaddress+"',"+getDocphno+",'"+getDocemail+"')")
doctor.commit()
doctor.close()
print("table created and inserted the pateint and doctordata")





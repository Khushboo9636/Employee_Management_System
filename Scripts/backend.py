import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="employee");
c=mydb.cursor();
login =False;
eid =input("Enter employee ID:");
pwd=input("Enter passwor");
c.execute("select * from emp")
#To retrive data
for row in c:
    if(eid==row[0] and pwd ==row[6]):
        login= True;
        break;
if(login):
    print("login successful");
else:
    print("Incorrect ID or password");


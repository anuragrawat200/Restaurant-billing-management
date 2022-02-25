import mysql.connector
conn = mysql.connector.connect(
  host="localhost",
  username="root",
  password="",
  database="billing_management",
   
)
cursor = conn.cursor()
cursor.execute("CREATE TABLE EMP_DETAILS(EID INT(10) PRIMARY KEY, NAME VARCHAR(20), PASSWORD VARCHAR(20), PHNO INT(10) UNIQUE)")
cursor.execute("CREATE TABLE ADMIN_DETAILS(AID INT(10) PRIMARY KEY, NAME VARCHAR(20), PASSWORD VARCHAR(20), PHNO INT(10) UNIQUE)")
cursor.execute("CREATE TABLE ITEM_DETAILS(IID INT(10) PRIMARY KEY, NAME VARCHAR(20), COST VARCHAR(20))")
cursor.execute("CREATE TABLE BILLS(DATETIME VARCHAR(40), EID INT(20), AMOUNT DOUBLE, REFNO INT(10))")
cursor.execute("CREATE TABLE DELETED_BILLS(DATETIME VARCHAR(40), EID INT(20), AMOUNT DOUBLE, REFNO INT(10))")
cursor.commit()

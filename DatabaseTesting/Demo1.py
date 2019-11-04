import pymysql

# CONNECT TO DATABASE
db = pymysql.connect("localhost","root","NmiSM2P","OnlineMusicStore" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")


# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Connected!")
print ("Database version : %s " % data)

# disconnect from server
db.close()
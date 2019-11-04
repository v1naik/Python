import pymysql

# CONNECT TO DATABASE
db = pymysql.connect("localhost","root","NmiSM2P","OnlineMusicStore" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
query1 = "SELECT * FROM Track"

cursor.execute(query1)

for cols in cursor:
    print(cols[0], "    ", cols[1], "         ", cols[2])

cursor.close()
db.commit()
db.close()

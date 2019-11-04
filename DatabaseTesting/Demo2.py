import pymysql

# CONNECT TO DATABASE
db = pymysql.connect("localhost","root","NmiSM2P","OnlineMusicStore" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
query1 = "INSERT INTO Track (TrackID, Tname, AlbumId, MediatypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice) VALUES (13, 'To the moon and back', 1, 1, 1, 'Savage Garden', 199836, 6566314, 1.99)"
query2 = "update query"
query3 = "delete query"
cursor.execute(query1)

cursor.close()
db.commit()
db.close()

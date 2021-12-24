import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

mycursor = mydb.cursor()


print('Database creation')
mycursor.execute("CREATE DATABASE mydatabase4")



print('\n\nShowing databases')
# mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

# ----------------------------- Create

mycursor.execute("CREATE TABLE customers2 (name VARCHAR(255), address VARCHAR(255))")


query = "SHOW TABLES"
mycursor.execute(query)

for x in mycursor:
  print(x)

################################


sql = "INSERT INTO customers2 (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

###############################

#mycursor = mydb.cursor()

sql = "INSERT INTO customers2 (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


# ----------------------------- Selecting

print("\n\n")

mycursor = mydb.cursor()

sql = "SELECT * FROM customers2 ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# ----------------------------- Deleting

sql = "DELETE FROM customers2 WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

# ---------------------------- Drop Tables

sql = "DROP TABLE customers2"

mycursor.execute(sql)
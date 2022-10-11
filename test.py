import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table="CREATE TABLE users(id int,username text,password text)"
cursor.execute(create_table)

user= (1,'vijaya','gavi')
insert_query="INSERT INTO user VALUES(?,?,?)"
cursor.execute(insert_query,user)


user= [(2,'guru','gavi'),(3,'nagesh','gavi')]

cursor.executemany(insert_query,user)

select_query="SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()



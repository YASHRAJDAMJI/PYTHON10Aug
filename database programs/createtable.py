import MySQLdb

try:
    query="create table stdinfo(name varchar(50),email varchar(40),address varchar(40))"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stdbs")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
   # query="create table stdinfo(name varchar(50),email varchar(40),address varchar(40))"
    cur.execute(query)
    print("execute query")
    mycon.commit()
    print(query+"table created .... ")
except:
    print("values inserted...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection")
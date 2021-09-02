import MySQLdb

try:
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stdbs")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="insert into stdinfo values('sdf','sdf@gmail.com','solapur') "
    cur.execute(query)
    print("execute query")
    mycon.commit()
    print(query+"sucessfully inserted values in table.... ")
except:
    print("values inserted...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection")
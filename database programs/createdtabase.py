import MySQLdb

try:
    query="CREATE DATABASE studentdb "
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
   
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
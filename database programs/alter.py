import MySQLdb

try:
    
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stdbs")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="alter table stdinfo add phno int(10)"
    cur.execute(query)
    
    print("execute query")
    mycon.commit()
    print(query+"table altered .... ")
except:
    print("table altered...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection")
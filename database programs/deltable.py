import MySQLdb

try:
    
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stdbs")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="drop table stdinfo"
    cur.execute(query)
    
    print("execute query")
    mycon.commit()
    print(query+"table Droped .... ")
except:
    print("table not Droped...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection")
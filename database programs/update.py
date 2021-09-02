import MySQLdb

try:
    
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stdbs")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="update stdinfo set address='pune' where name='sdf' "
    cur.execute(query)
    
    print("execute query")
    mycon.commit()
    print(query+"table updated .... ")
except:
    print("values updated...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection")
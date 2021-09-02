import MySQLdb

try:
    
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stdbs")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="select * from stdinfo"
    cur.execute(query)
    
    print("execute query")
    #mycon.commit()

    tdata=cur.fetchall()
    print("Records are ")
    for row in tdata:
        print("name : ",row[0])
        print("email : ",row[1])
        print("address : ",row[2])

except:
    print("values updated...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection")
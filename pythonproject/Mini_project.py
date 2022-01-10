import MySQLdb



def database():
    print("")
    print("Welcome to the generate console base invoice ")
    print(" 1] add products \n 2] show product \n 3] generate invoise bill \n 4] Exit ")
    ch=int(input("\nEnter your choice "))
    print("")
    print("----------------------------------------------------")
    
    if ch==4:
        print("_____________________EXIT___________________________")
    

    while (ch!=4):
        
        if ch==1:
            print("\nYou have selected Add products")
            print("\n Enter products info ")
            

            try:
                mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="pregi")
                
                regno=(input("\n Enter Product name :- "))
                pname=(input("\n Enter product id :- "))
                page=(input("\n Enter Price of product :- "))
                
                #INSERT INTO table-name (column-names) VALUES (values) ;
                query="""INSERT INTO productinfo (regno,pname,page) VALUES ('{}', '{}', '{}');""".format(regno,pname,page)
                cur=mycon.cursor()
                #vals=(pname,pid,pprice)
                cur.execute(query)
                mycon.commit()
                cur.close()
                #INSERT INTO productinfo (regno,P_name,dob,page,gender,pno,email,address) VALUES (1234,"abcd","25/02/89",89,"mail",1234567890,"abcd@gmail.com","solapur");
                
                database()
                break
            except:
                print("unable to insert ")
            
        if ch==2:
            print("\n You have selected show product ")
            try:
                mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="products")
                
                cur=mycon.cursor()
                
                query="select * from productinfo"
                cur.execute(query)
                
                
                #mycon.commit()

                tdata=cur.fetchall()
                print(" \n Records are ")
                print("__________________________")
                for row in tdata:
                    print("Id : ",row[0])
                    print("Name : ",row[1])
                    print("Price : ",row[2])
                    print("\n -------------------------")
                database()
                break
            except:
                print("unable to insert ")

        if ch==3:
            print("\nGenarated invoise bill\n")
            
            
            try:
                
                mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="products")
                cur=mycon.cursor() 
                
                query="select * from productinfo"
                cur.execute(query)
                
                
                #mycon.commit()
                price=0
                tdata=cur.fetchall()
                print("---------------------YOUR BILL---------------------\n")
                for row in tdata:
                    print("Id : ",row[0],"\tName : ",row[1],"\t  Price : ",row[2],"\n")
                    #print("Name : ",row[1])
                    #print("Price : ",row[2])
                    price=price+row[2]
                print("___________________________________________________")  
                print("Total :- \t\t\t\t  ",price)
                print("___________________________________________________")
                database()
                break
               
            except:
                print("unable to Genarate Bill")

        

database()



    





    

        
        
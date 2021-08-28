# quation 3 ] Write programm to read file and make Arithematic operation using file content.(File attached : "math.txt")


f=open("math.txt",'r',encoding='utf-8')
x=f.readlines()
y=x[0].split()
print(y)

add=0
sub=0
mul=0


for i in y:
    print(i)
    add = add + int(i)
    sub = sub - int(i)
    mul = mul * int(i)

print("\nAddition is: ",add)
print("\nSubstraction is: ",sub)  
print("\nMultiplication is: ",mul) 

#overflow error

a=200.76
b=1111111111111111111111111111.78

try:
    print("the addition is ",a**b)
except(OverflowError):
    print("overflow error ocured")

#divide by zero

b=0
try:
    print("Division by zero ",a/b)
except(ZeroDivisionError):
    print("divide by zero error ")

#value error

try:
    b=int(input("Enter teh variable to raise the Value eroorr"))
except(ValueError):
    print("Value Error")

#UnboundLocal Error

try:
    def f():
        a = a + 1
    f()
except (UnboundLocalError):
    print ("UnboundLocal Error")



#Type Error
a='2'
b=2
try:
    print("a+b",a+b)
except(TypeError):
    print("type error ")    

# Name error
d=10
g=7
try:
    print("Div",d+c)
except(NameError):
    print("name error ")

#indrntation


def f():
  pass

try:
    f()
except(IndentationError):
    print("error")


#syntax error
amount = 10000
try:
    if(amount > 2999)
    print("You are eligible to purchase gold")
except:
    print("This is syntax error"



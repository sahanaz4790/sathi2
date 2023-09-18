x ="potato","brinjal","mango","painapple","orange",
y =" world"
a = " shahanaz"
z = y +  " " +a

print(x[2])
print(x[2:4])
print(x[0:6:2])
print(y[1:4]+ " " +"banana")
print(z)
print(a*2)
print('s'   in  a)
amount = int(input(" enter your amount"))
message =" your current blance is {} taka".format(amount)
print(message)

amount = int(input("enter your amount:"))
message = " your current blance is %d taka"% (amount)
print(message)

amount = int(input("enter your amount:"))
message = f"your current blance is (amount)taka" 
print(message)

user_input = input("enter any chracter:")
x =len(user_input)
if x>=8:
 print("welcome")
else:
    print("invalid username")

user_input = input("enter any chracter")
z=len(user_input)
if z<=10:
    print("welcome")
else:
    print("invalid username")

user_input =input("enter any chracter")
print(user_input.lower())


user_input =input("enter any chracter")
print(user_input.upper())

user_input =input("enter any chracter")
print(user_input.swapcase())

user_input =input("enter any chracter")
print(user_input.capitalize())

user_input =input("enter any chracter")
x = user_input.split()
print(x)

user_input =input("enter any chracter")
x = user_input.split()
print(len(x))





        

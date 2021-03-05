my_favorite_animal='flying squirrel'
my_favorite_number =10
print(type(my_favorite_animal))
print(type(my_favorite_number))
print(my_favorite_animal)
print(my_favorite_number)
print(my_favorite_number//3) #integer div
print(my_favorite_number%3) #remainder
full_name = "john \nDoe"
print(full_name)
middle_name = 'O\'rielly'
print(middle_name)
print('hello'+' there')
print('hello there '*3)
my_name='Liliana'
age =100

print("Hi my name is "+ my_name)
print('I am teaching WDI {}, it is {}'.format(age,middle_name))
print(f'I am teaching WDI {age}, it is {middle_name}')
print(2==2)
print(2==3)
print(2=='2')
bolTest= 2=='2'
print(f'test, {bolTest}')
#print(f'test, {2=='2'}') does not work
x=10
y=20
print(x==10 and y==20)
print(x==10 or y==20)
print(not(x==10 or y==20))
print(type(None))
#print("Welcome to the Iron Rattler! How tall are you (in feet)?")
#height = int(input())
height = int(input('How tall are you?'))
if height < 4:
    print("Sorry, you'll fly out of your seat if we let you on.")
elif height>4 and height < 7:
    print("All aboard!")
else:
    print("If you value your head, you should not get on this ride.")
    
name = input('What is your name?')  
print(name)
num = int(input('what is number?'))
print(num)
print(type(None))
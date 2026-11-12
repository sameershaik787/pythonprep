#strings
print("hello sameer ")#my first print st
name='sameer';
food='biryani';
print(f"{name}")
print(f"{food}" , "he likes biryani")
 # print email
mail="sameer.edu@gmail,com";
print(f" your email is : {mail}")

#integers
age=20;
print(f"your age is :{age}")
students=20;
print(f"the no.of students in the class are : {students}")

  # floats
price=2.33;
print(f"the price of the item is : {price}")
#float
price=25;
print(f"the price of the product is :{price}")
#booleans
is_online=False;
if is_online:
    print("You are online")
else:
    print("you are not in online")

#typecasting
gpa=20
name="shaiksammer"
price=20
is_student=True
name=bool(name)
print(f"{name}")
gpa=int(gpa)
print(gpa)
name=str(name)
print(name)

#input from user
name = input("Enter your name: ")
age = int(input("Enter your age: ")) + 1

print(name)
print(f"Your age next year will be: {age}")






#assigning and reassgning the variables

city="jaipur";
print( city)

city="udaipur";
print(city)

# error check variables
st_score = 85
user_name = "Aarav"
totalscore = 100
print(st_score, user_name, totalscore)

#swapping variables Given a = 15 and b = 42, swap their values in a single line of Python so that a becomes 42 and b becomes 15. Print both variables afterward.

x=15
y=45
x,y = y, x
print(x,y)

#typecasting and string formatting
item_price=250
print(item_price)
quantity=3
print(quantity)
final_cost=item_price*quantity
print(f" {final_cost}")

#2nd way to writeConvert item_price to an integer, calculate the total cost, and store it in a variable called total_cost. Print the result using an f-string so it outputs: Total cost: 750.
item_price="250"
quantity=3
final_cost=int(item_price)*quantity
print(f"{final_cost}")

#coordinates Unpack the list coordinates = [26.9124, 75.7873] into two separate variables named latitude and longitude in one line. Then print each variable on its own line.

coordinates=[26.914,75.7830]
lattitude,longitude=coordinates
print(f"{coordinates}")

#
count = 10

def update_count():
    count = 25
    print("Inside function:", count)

update_count()
print("Outside function:", count)


#area of a rectangle
length = float(input("Enter the length of the item: "))
breadth=float(input("enter a number : "))
area=length*breadth
print(f"{area}")
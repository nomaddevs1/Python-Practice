from this import d


message = "hello world."
print(message.title())


first_name ="adam"
last_name ="lovelace"

#F-string
full_name = f"{first_name.title()} {last_name.title()}"
print(full_name)

#Stripping of whitespace
print(" hello ".strip())

#Excersise
#Personal Message
name = "adam"
message = f"Hello {name.title()}! Would like to like Python today?"
print(message)


#Name case
print(name.title())
print(name.upper())
print(name.lower())

#Famous Quote
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

famous_person = "Albert Einstein"
print(f'{famous_person} once said, "A person who never made a mistake never tried anything new."')

#Zen of Python
#import this
# print(this)

#List 
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles[0].title())

#insert methods allow item to be added in the list at any position
color = []
color.insert(1,"#ff0000")
print(color[0])
#Reversing thr bicycle list-
bicycles.sort(reverse=True)
print(bicycles)

#getting the length of the list
#the len function returns the length of the list
print(len(bicycles))

#sorted function can be used to sort the list
print(sorted(bicycles))
#reversing the list using the sorted function
print(sorted(bicycles, reverse=True))

#Exercises
#1.
#Create a list of the 5 places in the world you'd like to visit.
places = ["bali", "paris", "london", "new york", "tokyo"]
print(places)
places.reverse()


#Working with lists
#looping
#for in loop works like the for-in in javascript
magicians = ["alice", "david", "carolina"]
#It doesn't use curly braces to represent block scope instead  a ":" is used with indentation
for magician in magicians:
    #for block scope python use ";"
    if(len(magician) <= 5):
        print(magician)
for value in range(0 , len(magicians)):
    print(magicians[value]);

#tTools for a lis containg numerical values
#range funcion allows us to generate a series of numbers 
    #it will only print number between the first number parameters inclusive and the second parameter exclusively 
isPrime = True
number = 19

for value in range(2, number):
    if  number % value == 0:
        isPrime = False
    break

if isPrime == True:
        print(f"{number} is a prime number")
elif isPrime == False:
        print(f'{number} is not a prime number')
else:
        print("Bad number provided")
    
#Multiple usage of range 
#1-passing one argument
range(6) #print from 0 -5
#2-we can use range to form a list of number by using the list function
number = list(range(2, 11, 2)) #the third arg is going to be the difference between each number in the list. This makes the list a prime number 
print(number)

#for loop for creating squares
squares = []
for value in range(1, 11):
    # the "**" operator is used to do raise to power
    squares.append(value **2)
print(squares)
#other way of doing this is through list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)

#Exetcises
#1-odd-numbers
print(range(1, 20, 3))
#2-threes
threes = [three *3 for three in range(1, 11)]
print(threes)
#3-cubes
cubes = [cube **3 for cube in range(1, 11)]
print(cubes)




#Working with part of list 

#Slicing a list 
print(cubes[0:4])

players = ["charles", "martina", "micheal", "florence", "eli"]
print(players[:3])
print(players[-3:])

#We can do for loop for a slice list just place in a fot loop
for name in players[-3:]:
    print(name.title())
print("The list of players at the bottom of the table")

#Copying list
my_foods = ["pizza", "falafel", "carrot cake"]
friend_food = my_foods[:]

#Tuples- list that cannot be changed
dimensions = (200, 50)
print(dimensions[0])
# dimensions[1] = 20 # will throw an error because tuples are not mearnt to be chamge
#if we want to define a  tuple with one value it must have a trailing comma
my_t = (3,)

#Looping in a tuple is the same as looping in a list
for dimension in dimensions:
    print(dimension)

    #If statement
    #checking for equality
    car = "Bmw"
    car == "bmw"



#in keyword-> is used to check if an element is present in a lists
name = "marie"
banned_name = ["jake", "audrey", "melina"]
if name in banned_name:
        print("Name is banned you cannot access the content")
else:
        print("You can access the content")
  
#Dictionaries
alien_0={"color":"green", "points": 5}
print(alien_0["color"])
print(alien_0.items())
# We can add new key value pairs to the dictionary
alien_0["x-position"] = 0;
alien_0["y-position"] =25;
# a dicitionary retain the order it is defined
# a dicitionary key can be redefined by passing it another value
alien_0["color"] = "yellow"
print(alien_0.values())


# we can delete a key value pair by using the del keyword in front of the acccesor
del alien_0["points"]
print(alien_0)

#if a key doesn't exits in a dictionary we can use get method to specify what message we want back from the comp
print(alien_0.get("points", "Point key doesn't exist"))

# Looping through a dictionary
print(alien_0.items())
# we use the .items() method in a for loop to get both the key and value pair together
for k, v in alien_0.items():
    print(f"{k }:{ v}");
#Looping through a dicitionary the default behaviour is looping through the keys in the dictionary
for k in alien_0:
    print(f"{k}")  #This will print out all the keys in the dictionary
    # we can choose to use .keys() explicit if we want to make the code more readable

favorite_languages = {
    "jen" : "python",
    "sarah":"c",
    "edward":"ruby",
    "farouq":"javascript",
    "phil":"python"
}


for name in favorite_languages:
    if 'erin' not in name:
        print("Erin, please take our poll")

def twosums(arr, target):
    left = 0;
    right = len(arr)-1
    while(left <=  right):
        sum =arr[left]+arr[right];
        if(sum == target):
            return [arr[left], arr[right]]
        if(sum >  target):
            right= right-1
        else:
            left=left+1


print(twosums([1,3,4,5,7,11], 10))
 
import turtle
import colorsys 
t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor('black')
t.speed(0)
n=80 
h=0;

for i in range(360):
    c=colorsys.hls_to_rgb(h, 0.7, 0.8)
    h+=1/n
    t.color(c)
    for j in range(2):
        t.fillcolor('violet')
        t.left(20)
        t.color()
        t.forward(i*2)
    for v in range(3):
        t.left(70)
        t.forward(i*2)

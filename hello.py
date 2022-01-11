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
import this
# print(this)

#List 
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles[0].title())

#insert methods allow item to be added in the list at any position
color = []
color.insert(1,"#ff0000")
print(color[0])
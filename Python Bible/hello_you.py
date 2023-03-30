# ask user for their name
name=input("what is your name ? : ")
# print(name)
# ask user for their age
age=input("How old are you ? : ")
# print(age)
# ask user for their city
city=input("Where do you live ? : ")
# print(city)
# ask users what they enjoy
love=input("what do you love ? : ")
# print(love)
# create output text
string="your name is {} and you are {} years old. you live in {} ans you love {}"
output=string.format(name,age,city,love)
# print output to screen
print(output)

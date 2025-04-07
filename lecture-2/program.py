
# !
# ways to write strings in python
name = 'Piyush'
username = "thisIsMyUsername"
sentence = """Hello, I'm a valid string ..."""

# \n
# \t

# concatination
# print(name + username + sentence)
finalStr = name + username + sentence
# print(finalStr)

# print(len(finalStr))

# Indexing and slicing
str_one = "thisIs_A_String"
print(str_one[0])

print(str_one[ :4]) #slicing
print(str_one[1: len(str_one)])

# negative indexing bhi hota ha isme
# software enginner

# endswith()
print(str_one.endswith("ing"))

# capitalize
print(str_one.capitalize())

# replace
print(str_one.replace("_A_", "NotA_"))

# find
print(str_one.find("Is"))

# count
print(str_one.count("A"))

# practice
# username = input("Please enter your name: ")
print("Hello", username.capitalize(), "\nThere are total", len(username), "numers of characters!")

iAmDollar = "hello $ myself $$$ thats for that, $"
print(iAmDollar.count("$"))

# * if elif else

# practice
# WAP to check entered number is even or odd

# stoNum = int(input("Enter a number to check: "))
# if(stoNum % 2 == 0):
#     print(stoNum, "is even")
# elif(stoNum % 2 != 0):
#     print(stoNum, "is odd")


# largest of 3 numbers
# number1 = int(input("Enter 1st num: "))
# number2 = int(input("Enter 2nd num: "))
# number3 = int(input("Enter 3rd num: "))

# if(number1 > number2 and number1 > number3):
#     print("number1 is gratest", number1)
# elif(number2 > number3):
#     print("number2 is largest")
# else:
#     print("number3 is largest")


# number_a = int(input("Enter 1st num: "))
# number_b = int(input("Enter 2nd num: "))
# number_c = int(input("Enter 3rd num: "))
# number_d = int(input("Enter 4th num: "))

# if(number_a > number_b and number_a > number_c and number_a > number_d):
#     print(number_a,"is graeatest among", number_a, number_b, number_c, number_d)
# elif(number_b > number_a and number_b > number_c and number_b > number_d):
#     print(number_b,"is graeatest among", number_a, number_b, number_c, number_d)
# elif(number_c > number_a and number_c > number_b and number_c > number_d):
#     print(number_c,"is graeatest among", number_a, number_b, number_c, number_d)
# else:
#     print(number_d,"is graeatest among", number_a, number_b, number_c, number_d)

# check if any number is a multiple of 7 or not
x_val = int(input("Enter number: "))
if (x_val % 7 == 0):
    print("It is a multiple of 7")
else:
    print("Not a multiple of 7")

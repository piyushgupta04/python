# lists and tuples
marks = [43, 546, 7, 547, 333, 76]
print(marks)
print(type(marks))
print(len(marks))
print(marks[1])

food = ["eggs", "protein", "aloo", "creatine", "triceps"]
price = [345, 6534, 536, 37, 234]
print(food)
print(food[1:4])
# lists are mutlable matlab change kia ja sakta ha

# negative index bhi hoti ha

# * list methods
# append
# sort | reverse=True
# reverse
# insert

food.append("aloo")
price.sort(reverse=True)
print(price)
food.reverse()
print(food)

food.insert(1, "cucumber")
print(food)

# remove
# pop

food.remove("aloo")
print(food)

food.pop(4)
print(food)

food[4] = "bhujiya"
print(food)

# tuple
tup = (1, 4, 6, 23, 5, 6)
print(tup)
print(type(tup))

# slicing | same ha
print(tup[1:len(tup)])

# index
print(tup.index(23))

# count
print(tup.count(6))
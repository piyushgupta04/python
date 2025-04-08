# Python program
# dictionary-

information = {
    "key": "value",
    "name": "Piyush",
    "learning": "coding",
    "age": 21,
    "isAdult": True,
    "decimal": 43.556,
    "list": ["python", "javascript", "tailwind"],
    "topics": ("dictionaries", "sets"),
    45: "numeric key",
    4.5: "floating key",
    False: "boolean key",
    # kissi bhi type ki key ban sakti ha
}
print(information)
print(type(information))
# dist are unordered, mutlabe and can't create duplicate keys

print(information["learning"])
print(type(information["topics"]))
print(type(information["isAdult"]))

# adding key and value 
information["name"] = "Piyush"
information["surname"] = "Gupta"

print(information)

null_dict = {

}

print(null_dict)

# nested dictionaries
dict = {
    "name": "dict-alphabets",
    "info": {
        "a": "apple",
        "b": "ball",
        "c": "cat",
    }
}

print(dict["info"]["a"])
print(dict.keys())
# printing the keys of dictionary 'dict'
print(list(dict.keys())) # added len to get number of keys
print(list(dict.values()))

# ! https://youtu.be/078tYSD7K8E?si=eKY_tXOCvnzczxSh
# ! Brain not braining

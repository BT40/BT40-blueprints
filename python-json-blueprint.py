import json

print ("Program started")


#python to json

# a Python object (dict) storing saved states:
pyArray = {
  "name": "ortealPyCounter saves",
  "previous": 30,
  "zerow": 0,
  "theme": 0
}

print ("Python array created")


# convert python Array into JSON:

print ("Creating json array")

jsnArray = json.dumps(pyArray)

print ("json array created, here it is:")

# printing the result - a JSON string:
print(jsnArray) 



#json to py

print ("Now json to python")

# some JSON:
jsonx =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(jsonx)
# the result is a Python dictionary:


print ("Printing age from array;")

print(y["age"])  # printing only one value

print ("Printing whole array below:")

print(y)  # printing all values; whole array

print ("Exiting after successful run")











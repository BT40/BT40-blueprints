import pickledb

print ("Program started")

# Creating or loading database
db = pickledb.load('example.db', False)

# Adding new entry
db.set('key1', 'value1')

db.set('key2', 'value2')

# Fetching data entry from database (fetching in memory)
gv=db.get('key1')

gv2=db.get('key2')

# Fetching whole database
gvall=db.getall()

# writing or saving data to file
print ("will start writing to file")
db.dump() 
print ("Successfully saved to file")

# Printing entries
print ("Below is value of key1")
print (gv)

print ("Below is value of key2")
print (gv2)

print ("Below is after appending")

# appending something to existing 
db.append('key2', ' Something appended to value 2 ')

st2=db.get('key2')

print (st2)

print ("Exiting after successful run")










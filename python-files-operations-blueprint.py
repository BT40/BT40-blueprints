print ("Program started")

#vfo means variable for opening file. 
#Extra print commands have implemented to see progress in terminal. Put  hash to comment them out.


#Code to open or create file
print ("creating or opening  file")
vfo = open("blankdemofile.txt", "a+")
# a+ mode is for read and write, automatically creates file if not existing.
# by default cursor is at last, printing will result blank in terminal. Use seek function to mode curser to start.


# To close a file
vfo.close()


# To write contents to existing file, append mode, will not delete existing content
vfo = open("demofile.txt", "a+") # opening in a+ mode is necessary
# by default cursor is at last, printing will result blank in terminal. Use seek function to mode curser to start.
vfo.write("Now the file has initial content")
vfo.close()
print ("Closed file after first write")

#open and read the file after appending:
print ("Opening file after first write")
vf2 = open("demofile.txt", "a+")
vf2.seek(0)
print(vf2.read()) 
print ("Above are contenf of file after first write")

# below command has nothing to do with files
print ("Now Exiting after successful run")














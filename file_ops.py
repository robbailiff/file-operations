"""
Simple code created whilst playing around with basic file operations in the Sololearn playground.

"""

print("If we open a file in write mode, we can write to the file (clears all previous data) but not perform the read method on it.\n")

myfile = open("star_wars.txt", "w")
myfile.write("A long time ago in a galaxy far, far away...\n")

myfile.close()

print("If we open a file in append mode, we can add data to the end of a file without deleting previous content, but again we cannot read it.\n")

myfile2 = open("star_wars.txt", "a")
myfile2.write("Star Wars: Episode IV - A New Hope\n")

myfile2.close()

print("The default mode is read only if none are specified as the second argument. If we try to write data it will throw an error.\n")

myfile3 = open("star_wars.txt")

try:
    myfile3.write("It is a period of civil war. Rebel spaceships,striking from a hidden base, have won their first victory against the evil Galactic Empire.\n")
    
except Exception as e:
    print("Exception: " + str(e) + "\n")

myfile3.close()

print("If we use \"a+\" as the second arguent, we open the file in append and read mode which allows us to add data to the file and read it.\n")
    
myfile4 = open("star_wars.txt", "a+")

myfile4.write("It is a period of civil war. Rebel spaceships,striking from a hidden base, have won their first victory against the evil Galactic Empire.\n")

print("After data is written to a file, the location pointer within the file is present at the end after data. To read the file, you must first set the pointer back to the beginning of the file with the seek method.\n")

print("The read method returns the data as a string: \n")

myfile4.seek(0)
contents = myfile4.read()
print(contents)

print("\nYou can also use the readlines method to return the data as a list: \n")

myfile4.seek(0)
list_contents = myfile4.readlines()
print(list_contents)

myfile4.close()

"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

f = open('src/foo.txt', 'r')
# print(list(f))
for line in f:
    print(line, end="")
"""
f.read(size) : reads the file and returns it as a string (in text) or bytes obejct (in binary mode)
    - size : optional numeric arg // default is entire contents of the file
f.readline() : reads a single line from the file // newline character (\n) is left at the end of the string
for loop reading lines : loop over the file object // memory-efficient, fast, and leads to simple code
    - list(f) || f.readlines() : when you want to read all the lines of a file in a list
"""

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f2 = open('src/bar.txt', 'w')
f2.write('Writing for file2 overwrite?\n')
f2.write('2nd line\n')
f2.write('3rd line\n')

"""
f.open(filename, 'w') : create a file with the filename // if already exists, overwrite
f.write(string) : writes the contents of string to the file // return the number of characters written
"""
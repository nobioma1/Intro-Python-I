"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
foo_file = open('foo.txt', 'r')
foo_file_contents = foo_file.read()
print(foo_file_contents)
foo_file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar_file = open('bar.txt', 'w+')
bar_file.write('Writing my first lines in Python IO\n')
bar_file.write('Hello, Reader\n')
bar_file.write('Bye for now\n')
bar_file.close()

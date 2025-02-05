fp=open("text.txt", "r") #r is by default so not really needed
print(fp.read()) #prints the entire content of the file
fp.close() #good practice to close the file

#same exact thing with context manager
with open("text.txt", "r") as fp:
    print(fp.read())


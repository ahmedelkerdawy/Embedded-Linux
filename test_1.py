# python program to count number of lines in file

f = open(r"/home/ahmed-elkerdawy/Documents/01_python/tasks/tee","r") 
fd = f.readlines()
print(f"number of lines : {len(fd)}")

# python program to count number of words in file
xl = f.read()
print(f"number of words : {len(xl.split())}")


# python program to write list into file
students = ["name","age","id","email"]
fd = f.write(" ".join(students))
print(fd)
f.close()
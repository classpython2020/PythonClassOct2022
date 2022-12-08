# Files

#1. Sometimes we have to work on files data, may be we need to store some data in files, or we need to get the data
#   from files, and some new lines to files and all.
#2. There are three modes to do in python
    #1. write mode
    #2. Read mode
    #3. Append mode

#1. write mode
#1. Write mode will be used to write some data in the file.
#2. if alreay data in the file that will be over ride and add new data in that file.
#3. While we are writing data we need to mention w after the path.
#4. After complete the data we need to close that file by using close methode

f=open("C:\PythonClassOct2022\Python_class\Files\exmaple for files","w")  # we need to store this path in some variable.
f.write("1. This is raja yanamala\n")
f.write("2. This is raja yanamala\n")
f.write("3. This is raja yanamala\n")     #\n will be used for print the data in next line
f.write("4. This is raja yanamala\n")
f.write("5. This is raja yanamala\n")
f.write("6. This is raja yanamala\n")
f.write("7. This is raja yanamala\n")
f.write("8. This is raja yanamala\n")
print(f.writable())                   # it will give if the file is writable True or false.
print(f.writelines("9. This is raja yanamala\n"))    # it will add lines just like write
f.close()
print("program has completed")       # to know that program got completed without any errors.

# 2. Read mode

#1. we csan read the file by using read mode.
#2. to read the file we need to use print.
#3. to read we need to mention the r mode

f=open("C:\PythonClassOct2022\Python_class\Files\exmaple for files","r")
# print(f.read())   # by using read methode we can see total data what is inside of that file.
# print(f.readline())      #by using realine methode we can read only that fisrt line in the file.
print(f.readlines())      #by using this mothode we can spicify how many lines we want to read and they will come in list form.
# print(f.readable())        # if it is in read mode then only it will come true or false.
f.close()

# 3. Append mode

#1. we can add the data into files by using append mode.
#2. If we do same thing with write mode it will delete the old data and add new data in file.
#3. if we don't want to delete old data and add new data to it we have to use append mode.
#4. For that we need to use write methode but in append mode.


f=open("C:\PythonClassOct2022\Python_class\Files\exmaple for files","a")
f.write("\n10. This is raja yanamala\n")
f.write("11. This is raja yanamala")
f.close()
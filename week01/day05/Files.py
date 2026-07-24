
#Read a file
'''try:
    f=open("student.txt","r")
    print(f.read(10))
    print(f.readline())
    print(f.readlines())
    for line in f:
        print(line)
    f.close()
except FileNotFoundError:
    print("File does not exist")'''
with open("marks.txt","r") as f:
    print(f.read())

#write in a file
f=open("notes.txt","w")
f.write("python\nJava\nC++")
f.close()

#append in a file
f=open("notes.txt","a")
f.write("\nJavascript")
f.close()
try:
    with open("articles.txt","r") as f:
        a=f.read()
        with open("backup.txt","w") as f1:
            f1.write(a)

except:
    print("File does not exist")
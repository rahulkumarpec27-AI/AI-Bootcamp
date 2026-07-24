try:
    with open("articles.txt","r") as f, open("updated.txt","w+") as f1:
        set1=set()
        for line in f:
            if line not in set1:
                f1.write(line)
                set1.add(line)
        
except FileNotFoundError:
    print("Files does not exist")
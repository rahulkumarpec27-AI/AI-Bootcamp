try:
    with open("articles.txt","r") as f, open("updated.txt","w") as f1:
        for line in f:
            f1.write(line.replace("Python","AI"))

except FileNotFoundError:
    print("File does not exist")
    
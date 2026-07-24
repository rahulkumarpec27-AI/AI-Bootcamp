try:
    with open("articles.txt") as f, open("backup.txt") as f1:
        if f1.read()==f.read():
            print("Both files are same")
        else:
            print("files are not identical")
except FileNotFoundError:
    print("File does not exist")
        
try:
    with open("articles.txt","r") as f:
        dict1={}
        for line in f:
            line=line.strip()
            dict1[line] = dict1.get(line, 0) + 1
        for i in dict1:
            if dict1[i]>1:
                print(f"{i} -> {dict1[i]}")
except FileNotFoundError:
    print("Files does not exist")
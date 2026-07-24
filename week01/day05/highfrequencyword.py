try:
    with open("articles.txt","r") as f:
        dict1={}
        max1=0
        for line in f:
            line=line.strip('.\n')
            line=line.split()
            for i in line:
                dict1[i] = dict1.get(i, 0) + 1
                if dict1[i]>max1:
                    max1=dict1[i]
        for i in dict1:
            if dict1[i]==max1:
                print(f"{i} -> {dict1[i]}")
except FileNotFoundError:
    print("Files does not exist")
try:
    with open("articles.txt","r") as f:
        dict1={}
        for line in f:
            list1=line.strip('.\n')
            list1=list1.split()
            for i in list1:
                dict1[i]=dict1.get(i,0)+1
    
    for i in dict1:
        if dict1[i]==1:
            print(i)

except FileNotFoundError:
    print("file does not exist")
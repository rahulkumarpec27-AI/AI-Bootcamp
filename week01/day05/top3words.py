try:
    with open("articles.txt","r") as f:
        dict1={}
        for line in f:
            words=line.strip(".\n")
            words=words.split()
            for i in words:
                dict1[i]=dict1.get(i,0)+1
        sorted_list=sorted(dict1.items(),key=lambda x:x[1],reverse=True)
        counter=0
        sorted_dic={}
        for key,value in sorted_list[:3]:
            sorted_dic[key]=value
        print(sorted_dic)
except FileNotFoundError:
    print("File does not exist")
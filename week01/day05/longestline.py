try:
    with open("articles.txt",'r') as f:
        max1=0
        for line in f:
            line=line.rstrip()
            if len(line)>max1:
                max1=len(line)
                longline=line
        f.seek(0)
        for line in f:
            if len(line.rstrip())==max1:
                print(f"longest line is {longline} and the length of the line is {max1}")
except FileNotFoundError:
    print("file does not exist")
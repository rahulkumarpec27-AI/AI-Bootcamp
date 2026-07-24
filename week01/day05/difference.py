try:
    with open("articles.txt") as f1, open("updated.txt") as f2:
        count=0
        for line1,line2 in zip(f1,f2):
            count+=1
            if line1!=line2:
                print(f"Differnce found at {count}")
                print (f"file1 : {line1}")
                print (f"file2 : {line2}")
                

except FileNotFoundError:
    print("File does not exist")
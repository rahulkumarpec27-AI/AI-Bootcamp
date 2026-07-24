try:
    with open("articles.txt","r") as f:
        count=0
        for line in f:
            for ch in line:
                if ch.lower() in "aeiou":
                    count+=1
    print(f"Number of vowels are {count}")
except FileNotFoundError:
    print("file does not exist")
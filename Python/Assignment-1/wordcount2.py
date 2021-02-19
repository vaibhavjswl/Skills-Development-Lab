
file_name = str(input("Enter the File name : "))

try:
    search_word = str(input("Enter to word : "))
    search_word = search_word.lower()
    file=open(f"{file_name}.txt")
    file_text=file.read()
    file_text = file_text.split("\n")
    words=[]
    count=0
    for line in file_text:
        for word in line.split(" "):
            if word.lower() == search_word :
                count+=1

    print("\nWord count Results :\n")
    if count > 0:
        
        print(f"Word : {search_word} - Occurs {count} times in File : {file_name}.txt")
    else:
        print(f"Word : {search_word} - Does not Occurs in File : {file_name}.txt")
except:
    print("File not found please try again")





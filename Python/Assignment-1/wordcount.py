from collections import Counter

input_string=input("Enter a string : ")

word_counts = Counter(input_string.split(" "))
print(dict(word_counts))

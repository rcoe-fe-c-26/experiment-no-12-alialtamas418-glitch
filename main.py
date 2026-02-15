# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder: Altamash Ali
# Date:

print("--- Extracting Words from Text File ---\n")
# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths found within the file.
# Coder: Altamash Ali
# Date:

print("--- Extracting Words from Text File ---\n")


with open("story.txt", "r") as file:
    content = file.read()

length = int(input("Enter Length of Words: "))

words = content.split()

result = []

for word in words:
    if len(word) == length:
        result.append(word)

print(f"\nWords with length {length} are: {result}")




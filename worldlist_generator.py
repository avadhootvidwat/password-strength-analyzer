name = input("Enter name: ")
year = input("Enter birth year: ")
pet = input("Enter pet name: ")

patterns = ["123", "@", "2024", "!", "_"]

wordlist = []
for p in patterns:
    wordlist.append(name + p)
    wordlist.append(pet + p)
    wordlist.append(name + year)

with open("custom_wordlist.txt", "w") as f:
    for word in wordlist:
        f.write(word + "\n")

print("Custom wordlist generated successfully!")
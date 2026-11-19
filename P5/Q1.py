message = input("Enter a string: ").strip()

words = message.split()
acronmy = ""

for word in words:
    acronmy += word[0].upper()

print("The acronym for '{}'  is '{}'". format(message.strip(), acronmy))
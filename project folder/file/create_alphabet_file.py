import string

with open('alphabetFile.txt', 'w') as ab_file:
    ab_file.write(string.ascii_lowercase)

print("Alphabet file created.")
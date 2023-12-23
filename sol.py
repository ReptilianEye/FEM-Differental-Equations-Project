import string
for s in string.ascii_lowercase:
    if (string.ascii_lowercase.index(s) % 5 + 1 == 3):
        print(s.upper())

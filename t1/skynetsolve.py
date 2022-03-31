code = input("code: ")
code = code.split()
code.reverse()


for word in code:
    print(word, end=" ")
print(code)
for word in code:

    print(word, list(word)[0].isupper())
    if list(word)[0].isupper() == False:
        code.remove(word)
        print(code)

print("says: " + str((" ".join(code)).lower()))

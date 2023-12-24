flag = True
print(flag)


def main():
    # global scope to a flag variable & its applicable to all datatypes.
    global flag
    flag = False


main()
print(flag)

# del the  variable & it can access by other  functions.

del flag
print(flag=20)


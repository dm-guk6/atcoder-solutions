a = input()
b = 'abcdefghijklmnopqrstuvwxyz'

for s in b:
    if not s in a:
        print(s)
        break
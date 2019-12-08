string = bytes(input("Enter the string: "), 'windows-1251')

string = string.replace(b",", b"")
string = string.replace(b".", b"")
string = string.replace(b"!", b"")
string = string.replace(b"?", b"")
string = string.replace(b"-", b"")
string = string.replace(b" - ", b"")

word = string.split()
for k in word:
    len_word = len(k)
    print("%s" % k.decode('windows-1251') + "(%s) " % len_word, end="")
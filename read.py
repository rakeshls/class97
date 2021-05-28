intro=input("introduce yourself")
charcount=0
wcount=0
for i in intro:
    charcount+=1
    if (i==" "):
        wcount+=1
print("numbers of charcters are")
print(charcount)
print("numbers of words are")
print(wcount)

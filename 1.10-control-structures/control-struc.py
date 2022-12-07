wordlist = ['cat','dog','rabbit']
letterlist = [ ]

for aword in wordlist:
    for aletter in aword:
        if aletter not in letterlist: # if letter not in letter list will be true unless a duplicate is in the list
            letterlist.append(aletter) # append removes aletter put into new arr(letterlist)


print(letterlist)


list = ["soup", "shrimp", "taco"]
arr = [ ]

for i in list:
    for letter in i:
        if letter not in arr:
            arr.append(letter)

print(arr)
print(len(arr))

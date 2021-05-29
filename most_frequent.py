def most_frequent(let):
    if let in dict:
        dict[let] += 1

    else:
        dict.update({let : 1})

    return dict

x = input("enter a string")
dict = {}
for let in x:
    most_frequent(let)
for i in dict:
    print("%s : %s" % (i, dict[i]))

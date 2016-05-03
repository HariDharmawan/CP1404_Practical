dictionary = {}
text = "this is a collection of words of nice words this is a fun thing it is"

listings = text.strip().split()

for each in listings:
    if each in dictionary:
        dictionary[each] += 1
    else:
        dictionary[each] = 1

sorted_keys = sorted(dictionary)

for each in sorted_keys:
    print("{:10s} -> {:<5d}".format(each, dictionary[each]))

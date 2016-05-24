def sorting_word(dictionary, listings):
    """For sorting the word"""
    for each in listings:   #To iterate through the the word
        if each in dictionary:
            dictionary[each] += 1   #To add value if its already in dictionary
        else:
            dictionary[each] = 1    #To set value of 1 if it isnt in dictionary

    sorted_keys = sorted(dictionary)
    return sorted_keys


dictionary = {} #To make empty dictionary
text = "this is a collection of words of nice words this is a fun thing it is"

listings = text.strip().split() #To split the sentences word by word

sorted_keys = sorting_word(dictionary, listings)    #Run the function

for each in sorted_keys:    #Iterate through the object in the sorted dictionary
    print("{:10s} -> {:<5d}".format(each, dictionary[each]))    #Print it

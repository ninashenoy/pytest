def list_examples():
    
    #append
    list = ['apple', 'banana', 'cherry']
    list.append("grape")
    print(list)
    list2 = ['tomato']
    list.append(list2)
    print(list)

    #clear
    list.clear()
    print(list)

    #copy
    list = ['apple', 'banana', 'cherry']
    c = list.copy()
    print(c)

    #count
    c = list.count("apple")
    print(c) 

    #extend
    list.extend(list2)
    print(list)

    #index
    i = list.index("banana")
    print(i)

    #insert
    list.insert(2, "mango")
    print(list)

    #pop
    list.pop(2)
    print(list)

    #remove
    list.remove("apple")
    print(list)

    #reverse
    list.reverse()
    print(list)

    #sort
    list.sort()
    print(list)

    return

list_examples()
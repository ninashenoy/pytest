'''
from typing import ClassVar


def dictionary_examples():
    dog = {
        "name" : "leo",
        "breed" : "boxer",
        "age" : "4"
    }


    #copy
    temp = dog.copy()
    print(temp)

    #clear
    temp.clear()
    print(temp)

    #fromkeys
    key = ('dog', 'cat', 'bird')
    val = 1
    thisdict = dict.fromkeys(key,val)
    print(thisdict)

    #get
    x = thisdict.get("cat")
    print(x)
    

    #items
    x = dog.items()
    print(x)

    #keys
    x = dog.keys()
    print(x)

    #pop
    dog.pop("age")
    print(dog)

    #popitem
    dog.popitem()
    print(dog)

    #setdefault
    x = dog.setdefault("breed", "labrador")
    print(dog)

    #update
    dog.update({"color":"brown"})
    dog.update({"breed":"boxer"})
    print(dog)

    #values
    x = dog.values()
    print(x)

    return


dictionary_examples()
'''
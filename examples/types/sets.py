# Sets are a built in data type in python to store collections of data
# They can store multiple items into a single variable
# Sets are unordered and unindexed
# Sets cannot have two items of the same value
# Declared using curly brackets {}

def set_examples():

    #add
    fruit = {"apple", "banana", "orange"}
    fruit.add("grape")
    print(fruit)

    #clear
    nuts = {"peanuts"}
    nuts.clear()
    print(nuts)

    #copy
    fruit_c = fruit.copy()
    fruit_c.add("watermelon")
    print(fruit_c)

    #difference
    veg = {"carrot", "pea", "broccoli"}
    x = fruit.difference(veg)
    print(x)
    x = veg.difference(fruit)
    print(x)

    #difference_update
    fruit2 = {"banana", "mango", "passionfruit"}
    fruit.difference_update(fruit2)
    print(fruit)

    #discard
    fruit2.discard("mango")
    print(fruit2)

    #intersection
    nums1 = {1,2,3,4}
    nums2 = {1,2,10,20}
    print(nums1.intersection(nums2))

    #intersection_update
    nums1.intersection_update(nums2)
    print(nums1)

    #isdisjoint
    nums3 = {5,6,7,8}
    x = nums1.isdisjoint(nums3)
    print(x)

    #issubset
    nums1 = {1,2,3,4,5}
    nums2 = {2,4}
    x = nums2.issubset(nums1)
    print(x)

    #issuperset
    x = nums1.issuperset(nums2)
    print(x)

    #pop
    x = nums1.pop()
    print(x)
    print(nums1)

    #iterate
    for fr in fruit2:
        print (fr)












    return

set_examples()
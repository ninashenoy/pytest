import dictionary

def print_dictionary(snacks):
    keys = snacks.keys()
    for key in keys:
        val = snacks.get(key)
        print(key, end = " ")
        print(val)
    return

fruitslist =['apples', 'oranges', 'banana'] 
veglist = ['broccoli', 'carrot', 'peas']
nutslist = ['peanuts', 'almonds', 'cashews']

snacks = {
}

snacks.update({"fruits":fruitslist})
snacks.update({"veg":veglist})
snacks.update({"nuts":nutslist})

print_dictionary(snacks)
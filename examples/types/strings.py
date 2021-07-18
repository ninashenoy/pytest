
###############################################################################
def strings_example():
    h = "Hello"
    w = "World"
    hw = h + w
    print("h:: %s" % h)
    print("w:: %s" % w)
    print("hw:: %s" % hw)

    #compare
    if( h == w ):
        print("h::%s == w::%s are equal" %(h, w))
    else:
        print("h::%s != w::%s are NOT equal" %(h, w))

    print(type(h))
    
    hw="    Hello World   "
    #capitalize, upper, lower, lstrip
    temp = hw.capitalize()
    temp = hw.upper()
    temp = hw.lower()
    temp = hw.lstrip(" ")

    #rstrip
    temp = hw.rstrip(" ")

    #split will return a list of strings
    hw="Hello World   "
    temp = hw.split(" ")
    print(type(temp))
    index = 0
    for st in temp:
        print( "index%s::%s" % (str(index), st) )
        index=index+1

    #count
    num=hw.count("Hello")
    num=hw.count("l")

    #center
    var="banana"
    temp=var.center(20)

    #encode
    temp = hw.encode()

    #endswith
    hw = "Hello World"
    temp = hw.endswith("World")
    print(temp)

    #expandtabs
    temp = "H\te\tl\tl\to"
    temp.expandtabs(5)
    print(temp)

    #find
    temp = hw.find("l")
    print(temp)

    #format
    temp = "For only {price:.2f} dollars!"
    print(temp.format(price = 49.50))

    #index
    temp = hw.index("Wor")
    print(temp)

    #isalnum
    temp = "H#ll* W0rld"
    print(temp.isalnum())

    #isidentifier
    temp = "hello_world_"
    print(temp.isidentifier())

    #isspace
    temp = "     "
    print(temp.isspace())

    #join
    temp = ("Hello", "World")
    j = "$".join(temp)
    print(j)

    #partition
    temp = hw.partition("lo")
    print(temp)

    #replace
    temp = hw
    temp = temp.replace("l", "1")
    print(temp)

    #splitlines
    temp = "Hello\nWorld\nHey"
    temp = temp.splitlines()
    print(temp)

    #startswith
    temp = hw.startswith("He")
    print(temp)

    #strip
    temp = "asid0 hello 3892"
    temp = temp.strip("asdi03829 ")
    print(temp)

    #translate
    mydict = {83:  80} #replace 83(S) with 80 (P)
    txt = "Hello Sam!"
    print(txt.translate(mydict))

    #zfill
    txt = "hello"
    x = txt.zfill(10)
    print(x)
    return

strings_example()

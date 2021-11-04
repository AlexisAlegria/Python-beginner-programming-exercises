def number_of_bottles():
    x=99
    text1 = "bottles of milk on the wall, "
    text2 = " bottles of milk."
    text3 = "\nTake one down and pass it around, "
    text4 = " bottles of milk on the wall."
    text5 = "bottle of milk on the wall."

    text6 = " bottle of milk on the wall, "
    text7 = "bottle of milk."
    text71 = "\nTake one down and pass it around, no more bottles of milk on the wall."

    text8 = "No more bottles of milk on the wall, no more bottles of milk."
    text9 = "\nGo to the store and buy some more, "

    i=99
    while i > 0:
        if i!=1:
            print(str(i) + " " + text1 + str(i) + text2 + text3 + str(i-1) + text4)
        else:
            print(str(i) + text6 + str(i) + " " + text7 + text71)
        i=i-1
    
    print(text8 + text9 + str(x) + text4)

number_of_bottles()
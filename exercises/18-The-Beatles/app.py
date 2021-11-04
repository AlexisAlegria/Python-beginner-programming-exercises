# Your code here!!
def sing ():
    lib = "let it be"
    lib_plus = "\nlet it be"

    lyrics = lib + ","

    for i in range (3):
        lyrics += lib_plus + ","

    lyrics += "\nwhisper words of wisdom, "
    lyrics += lib + ", "
    lyrics += lib + ","

    for i in range(3):
        lyrics += lib_plus + ","
        
    lyrics += "\nthere will be an answer, "
    lyrics += lib

    print(lyrics)

sing()
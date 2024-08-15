def load():
    # load what u saved in var text, then print it
    file = open("test.txt", "r")
    text = file.read()
    print(text)
    file.close()


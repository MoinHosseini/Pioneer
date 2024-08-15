def loadParagraphs():
    print("Paragraphs saved is as below:")
    with open('paragraphs.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
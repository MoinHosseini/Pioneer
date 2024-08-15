def loadParagraphs():
    print("Paragraphs saved is as below:")
    with open('paragraph.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
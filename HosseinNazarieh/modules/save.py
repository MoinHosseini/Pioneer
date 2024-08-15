def saveParagraph():
    firstParagraph = input()
    secondParagraph = input()
    with open('paragraphs.txt', 'w') as f:
        f.write(firstParagraph)
        f.write(secondParagraph)
    print("Successfully created the paragraphs into the file.")
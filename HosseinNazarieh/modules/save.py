def saveParagraph():
    firstParagraph = input()
    secondParagraph = input()
    cntr = 40
    while cntr < len(firstParagraph):
        leftPart = firstParagraph[:cntr] + '\n'
        if cntr + 1 < len(firstParagraph):
            rightPart = firstParagraph[cntr:]
        firstParagraph = leftPart + rightPart
        cntr += cntr
    cntr = 40
    while cntr < len(secondParagraph):
        leftPart = secondParagraph[:cntr] + '\n'
        if cntr + 1 < len(secondParagraph):
            rightPart = secondParagraph[cntr:]
        secondParagraph = leftPart + rightPart
        cntr += cntr
    with open('paragraphs.txt', 'w') as f:
        f.write(firstParagraph)
        f.write(secondParagraph)
    print("Successfully created the paragraphs into the file.")
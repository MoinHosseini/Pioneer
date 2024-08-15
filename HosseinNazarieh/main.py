def main():
    print("Which one do you prefer to use today ?")
    print("1. Load the saved data from the file")
    print("2. Save two paragraphs into the file")
    print("3. Exit")
    cmd = input("Choose your desired number:")
    while cmd not in ["1", "2", "3"]:
        cmd = input("Invalid input, please try again:")
    match(cmd):
        case "1":
            from modules.load import loadParagraphs
            loadParagraphs()
        case "2":
            from modules.save import saveParagraph
            saveParagraph()

if __name__ == "__main__":
    main()
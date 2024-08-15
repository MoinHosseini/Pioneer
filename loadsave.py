import os
def save(text):
    with open('output.txt', 'w') as file:
        file.write(text)

text = "Lorem ipsum dolor sit amet veniam ad enim ut ut proident culpa consequat. Aliqua sed aliquip sunt proident eu anim. Aute proident pariatur laborum mollit fugiat ad nisi esse magna quis consequat. Ipsum exercitation dolor incididunt aliquip tempor enim veniam magna ut dolor aliquip veniam incididunt. In ullamco officia nostrud minim dolor sit pariatur.Cupidatat ullamco adipiscing do occaecat non officia commodo sit anim duis ad labore. Tempor ullamco lorem laboris sunt lorem sit excepteur in veniam qui. Magna esse in sint culpa in culpa qui ea ullamco. Commodo nulla duis anim duis adipiscing. Dolore proident elit id non cupidatat in commodo pariatur ut ut proident elit.Voluptate duis voluptate velit lorem do elit dolor. Dolor fugiat pariatur duis magna consectetur ut. Elit ipsum in eu aliqua in minim amet ex laboris labore laboris ut exercitation. Deserunt culpa magna adipiscing non ut eu. Veniam dolore amet et exercitation et elit aute sit dolor lorem labore."
save(text)

def load():
    if os.path.exists('output.txt'):
        with open('output.txt', 'r') as file:
            text = file.read()
        print(text)
    else:
        print("No saved file found.")

load()
def main():
    choice = input("Enter 1 to save text or 2 to load text: ")
    if choice == '1':
        text = input("Enter the text you want to save: ")
        save(text)
        print("Text has been saved.")
    elif choice == '2':
        load()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        
if __name__ == "__main__": 
    main()
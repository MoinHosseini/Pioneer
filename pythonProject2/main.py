import json
import pickle
import yaml


def load():
    # load what u saved in var text, then print it

    # load
    file1 = open("MyFile2.txt", "r")
    text = file1.readlines()
    print(text)
    file1.close()

def save(text):
    # sava
    file1 = open("MyFile2.txt", "w")
    file1.writelines(text)
    file1.close()

def serializePickle():
    # Pickle

    # Serialize
    data = {'name': 'John', 'age': 30}
    with open('data.pickle', 'wb') as file:
        pickle.dump(data, file)
def serializePickle(text):
    # Pickle

    # Serialize
    with open('data.pickle', 'wb') as file:
        pickle.dump(text, file)
def deserializePickle():
    # Deserialize
    with open('data.pickle', 'rb') as file:
        serialized_data = file.read()
        file.seek(0)
        loaded_data = pickle.load(file)

    print("Type of serialized data:", type(serialized_data))
    print("Deserialized data:", loaded_data)
    print("Type of deserialized data:", type(loaded_data), "\n")

def serializeJSON():
    # Pickle

    # Serialize
    data = {'name': 'John', 'age': 30}
    with open('data.json', 'w') as file:
        json.dump(data, file)
def serializeJSON(text):
    # Pickle

    # Serialize
    data = {'name': 'John', 'age': 30}
    with open('data.json', 'w') as file:
        json.dump(data
                  , file)
def deserializeJSON():
    # Deserialize
    with open('data.json', 'r') as file:
        serialized_data = file.read()
        file.seek(0)
        loaded_data = json.load(file)

    print("Type of serialized data:", type(serialized_data))
    print("Deserialized data:", loaded_data)
    print("Type of deserialized data:", type(loaded_data), "\n")

def serializeYAML():
    # YAML

    # Serialize
    data = {'name': 'John', 'age': 30}
    with open('data.yaml', 'w') as file:
        yaml.dump(data, file)
def serializeYAML(text):
    # YAML

    # Serialize
    data = {'name': 'John', 'age': 30}
    with open('data.yaml', 'w') as file:
        yaml.dump(data, file)

def deserializeYAML():
    # Deserialize
    with open('data.yaml', 'r') as file:
        serialized_data = file.read()
        file.seek(0)
        loaded_data = yaml.safe_load(file)

    print("Type of serialized data:", type(serialized_data))
    print("Deserialized data:", loaded_data)
    print("Type of deserialized data:", type(loaded_data))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x=1
    while x :
        n=int(input("load------>1\n"
                    "save------>2\n"
                    "serializePickle------>3\n"
                    "deserializePickle------>4\n"
                    "serializeJSON------>5\n"
                    "deserializeJSON------>6\n"
                    "serializeYAML------>7\n"
                    "deserializeYAML------>8\n"
                    "exit------>9\n"
                    "->"))
        text = "Lorem ipsum dolor sit amet veniam ad enim ut ut proident culpa consequat. Aliqua sed aliquip sunt proident eu anim. Aute proident pariatur laborum mollit fugiat ad nisi esse magna quis consequat. Ipsum exercitation dolor incididunt aliquip tempor enim veniam magna ut dolor aliquip veniam incididunt. In ullamco officia nostrud minim dolor sit pariatur.Cupidatat ullamco adipiscing do occaecat non officia commodo sit anim duis ad labore. Tempor ullamco lorem laboris sunt lorem sit excepteur in veniam qui. Magna esse in sint culpa in culpa qui ea ullamco. Commodo nulla duis anim duis adipiscing. Dolore proident elit id non cupidatat in commodo pariatur ut ut proident elit.Voluptate duis voluptate velit lorem do elit dolor. Dolor fugiat pariatur duis magna consectetur ut. Elit ipsum in eu aliqua in minim amet ex laboris labore laboris ut exercitation. Deserunt culpa magna adipiscing non ut eu. Veniam dolore amet et exercitation et elit aute sit dolor lorem labore."
        if n==1:
            load()
        elif n==2:
            save(text)
        elif n==3:
            serializePickle(text)
        elif n==4:
            deserializePickle()
        elif n==5:
            serializeJSON(text)
        elif n==6:
            deserializeJSON()
        elif n==7:
            serializeYAML(text)
        elif n==8:
            deserializeYAML()
        elif n==9:
            x=0
# See PyCharm help at https://www.jetbrains.com/help/pycharm/




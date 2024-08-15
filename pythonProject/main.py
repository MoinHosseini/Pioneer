import save
import load

while 1:
    inp = input()

    if inp.__eq__("w"):
        save.save(save.text)

    elif inp.__eq__("r"):
        load.load()

    else:
        break

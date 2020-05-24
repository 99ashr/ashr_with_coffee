import pickle

# my_randi = ["ananya", "vanisha", "neha", "arushi", "ashna"]
new_randi = [input("Name of new Randi:\t")]
randi = []


def writefunc():
    with open("myRandi.txt", "ab") as filehandle:
        pickle.dump(new_randi, filehandle)


def readfunc():
    with open("myRandi.txt", "rb") as filehandle:
        try:
            while True:
                randi.append(pickle.load(filehandle))
        except EOFError:
            pass
        print(randi)


writefunc()
readfunc()

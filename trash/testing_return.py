import pickle
import sys
import os
import emoji

all_repos = []
user_repo_link = "https://github.com/99ashr/"
remote = "git remote add origin"
repo_name = input("Enter the name of your repo!\nHere:\t")

print(repo_name)


def readfunc():
    with open("iamrapist.txt", "rb") as filehandle:
        try:
            while True:
                all_repos.append(pickle.load(filehandle))
        except EOFError:
            pass
        return all_repos[-1]
        # print(all_repos)


def writefunc():
    with open("iamrapist.txt", "ab") as filehandle:
        pickle.dump(repo_name, filehandle)
        print(repo_name)


if repo_name == "":
    try:
        repo_name = readfunc()
    except FileNotFoundError:
        print("please enter the name manually!")
        # sys.stdout.flush()
        # os._exit(0)
else:
    writefunc()


def connect_remote():
    # repo_name = readfunc()
    print(emoji.emojize("Connecting to your remote directory...:lying_face:"))
    # os.system("{} {}{}.git".format(remote, user_repo_link, repo_name))
    print("{} {}{}.git".format(remote, user_repo_link, repo_name))
    # print(repo_name)


connect_remote()

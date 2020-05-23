import os
import emoji


def current_dir():
    return os.getcwd()


# print(current_dir())

# print("{{{}}}".format(42))  # {42}


def creating_md():
    print("Creating README File for you!")
    print("Please Wait...")
    # print("\N{grinning face}")
    print(emoji.emojize(":zipper-mouth_face:"))


def git_init():
    print("Initializing the repository...")
    os.system("git init")


def my_git_cmd():
    pwd = current_dir()


if __name__ == "__main__":
    current_dir()
    creating_md()
    git_init()

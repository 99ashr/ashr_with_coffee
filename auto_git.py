import os
import emoji


repo_name = "ashr_with_coffee"
commit_msg = "testing commit msg"


def current_dir():
    return os.getcwd()


# print(current_dir())


def creating_md():
    print("Creating README File for you!")
    print(emoji.emojize("\nPlease Wait...:slightly_smiling_face:"))
    os.system("echo '# {}'>>README.md".format(repo_name))
    print(
        emoji.emojize(
            "\nCreated README.md successfully for you!:smiling_face_with_halo:"
        )
    )


def git_init():
    print(
        emoji.emojize(
            "\nInitializing your repository...:smiling_face_with_smiling_eyes:"
        )
    )
    os.system("git init")


def git_add():
    print(emoji.emojize("\n Initializing Git Add Command for you...:smiling_face:"))
    os.system("git add .")


def git_status():
    print(emoji.emojize("Here's the status of this REPO...:face_savoring_food:"))
    os.system("git status")


def git_commit():
    print(emoji.emojize("Ready To Commit Your MESS...?:expressionless_face:"))
    # os.system("git commit -m {}".format(msg))
    os.system("git commit")


def my_git_cmd():
    pwd = current_dir()


if __name__ == "__main__":
    current_dir()
    creating_md()
    git_init()
    git_add()
    git_status()
    git_commit()

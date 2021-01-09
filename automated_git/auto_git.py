import os
import emoji
import pickle
import pyttsx3


# &Create Object and Set voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # getting details of current voice
# changing index, changes voices. o for male
# engine.setProperty('voice', voices[0].id)
# changing index, changes voices. 1 for female
engine.setProperty('voice', voices[1].id)


# repo_name = "ashr_with_coffee"
all_repos = []


def talk(talk):
    engine.say(talk)
    engine.runAndWait()


talk("Please enter the name of your repository")
repo_name = input(
    emoji.emojize(
        "Enter the name of your repository here!:pensive_face:\nHere!:\t")
)


def writefun():
    with open("myRepos.txt", "ab") as filehandle:
        pickle.dump(repo_name, filehandle)


def readfun():
    with open("myRepos.txt", "rb") as filehandle:
        try:
            while True:
                all_repos.append(pickle.load(filehandle))
        except EOFError:
            pass
        return all_repos[-1]


def current_dir():
    return os.getcwd()


# print(current_dir())


def creating_md():
    # repo_name = readfun()
    print("Creating README File for you!")
    print(emoji.emojize("\nPlease Wait...:slightly_smiling_face:"))
    os.system("echo '# {}'>README.md".format(repo_name))
    print(
        emoji.emojize(
            "\nCreated README.md successfully for you!:smiling_face_with_halo:"
        )
    )


def git_init():
    talk("Initializing your repository")
    print(
        emoji.emojize(
            "\nInitializing your repository...:smiling_face_with_smiling_eyes:"
        )
    )
    os.system("git init")


def git_add():
    talk("Adding files to commit")
    print(emoji.emojize("\n Initializing Git Add Command for you...:smiling_face:"))
    os.system("git add .")


def git_status():
    talk("These files are added")
    print(emoji.emojize("Here's the status of this REPO...:face_savoring_food:"))
    os.system("git status")


def git_commit():
    talk("Ready To Commit")
    print(emoji.emojize("Ready To Commit Your MESS...?:expressionless_face:"))
    talk("Please enter your commit message")
    commit_msg = input(
        emoji.emojize(
            "Please enter your commit message here:drooling_face:\n message:")
    )
    commit = "git commit -m {}".format(commit_msg)
    os.system(commit)


user_repo_link = "https://github.com/99ashr/"
remote = "git remote add origin"


def connect_remote():
    # repo_name = readfun()
    talk("Connecting to your remote directory")
    print(emoji.emojize("Connecting to your remote directory...:lying_face:"))
    os.system("{} {}{}.git".format(remote, user_repo_link, repo_name))


def git_push():
    talk("We're good to go.")
    os.system("git push origin master")


if __name__ == "__main__":
    current_dir()
    if repo_name == "":
        try:
            repo_name = readfun()
        except FileNotFoundError:
            talk("oops something is wrong")
            print("please enter the name manually!")
    else:
        writefun()
    creating_md()
    git_init()
    git_add()
    git_status()
    git_commit()
    git_status()
    connect_remote()
    git_push()
    engine.stop()

import os
from git import Repo
from tkinter import Tk 
from tkinter.filedialog import askdirectory, askopenfilenames

git_url = r"https://github.com/openalea/openalea.rtfd.io"
output_folder = r"C:\Users\gandeell\Documents\GitHub\grapeinsilico.github.io\2.1\Convertisseur\openalea"

def clone_from_git(git_url, output_folder):
    """
    Clone a git repository from a url.
    :param git_url: url of the git repository
    :param output_folder: path of the output folder
    :return:
    """
    ## if the folder doesn't exist, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # the git repository has aleady been cloned
    if os.path.exists(os.path.join(output_folder, ".git")):
        print("The git repository has already been cloned")
        return
    repo = Repo.clone_from(git_url, output_folder)
    return repo

#clone_from_git(git_url, output_folder)

# function to ask for a directory
def ask_directory():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    directory = askdirectory(initialdir=os.getcwd(), title='Please select a directory')
    return directory

# function to ask for images
def ask_images():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    directory = askopenfilenames(initialdir=os.getcwd(), title='Please select a directory')
    # only keep image files
    images = []
    for image in directory:
        if image.endswith(".png") or image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith(".gif"):
            images.append(os.path.abspath(image))
    return images

# find file in tree
def find_file(path, filename):
    for root, dirs, files in os.walk(path):
        if filename in files:
            return os.path.abspath(os.path.join(root, filename))
    return ""

# find folder in tree
def find_folder(path, foldername):
    for root, dirs, files in os.walk(path):
        if foldername in dirs:
            return os.path.abspath(os.path.join(root, foldername))
    return ""

# change line in file that begins with text
def change_line(path, text, new_text):
    with open(path, 'r') as file:
        lines = file.readlines()
    with open(path, 'w') as file:
        for line in lines:
            if line.startswith(text):
                line = line.replace(text, new_text)
    return ""

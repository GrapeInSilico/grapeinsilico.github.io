import os
from git import Repo
from tkinter import Tk 
from tkinter.filedialog import askdirectory, askopenfilenames

def clone_from_git(git_url, output_folder):
    """
    Clone a git repository from a url.
    :param git_url: url of the git repository
    :param output_folder: path of the output folder
    :return: the cloned repository
    
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
    """
    Ask for a directory
    :return: the path of the directory
    """
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    directory = askdirectory(initialdir=os.getcwd(), title='Please select a directory')
    return directory

# function to ask for images
def ask_images():
    """
    Ask for images
    :return: the path of the images
    """
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
    """
    Find a file in a tree
    :param path: the path of the tree
    :param filename: the name of the file
    :return: the path of the file
    """
    for root, dirs, files in os.walk(path):
        if filename in files:
            return os.path.abspath(os.path.join(root, filename))
    return ""

# find folder in tree
def find_folder(path, foldername):
    """
    Find a folder in a tree
    :param path: the path of the tree
    :param foldername: the name of the folder
    :return: the path of the folder
    """
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

# clone branch from git
def clone_branch(git_url, branch_name, output_folder):
    repo = Repo.clone_from(git_url, output_folder)
    repo.git.checkout(branch_name)
    return repo

# clone folder from git
def clone_folder(git_url, folder_name, output_folder):
    repo = Repo.clone_from(git_url, output_folder)
    repo.git.checkout(folder_name)
    return repo


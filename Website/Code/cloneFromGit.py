import os
from git import GitCommandError, Repo
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilenames

# Clone a git repository from a url, ask for a directory and ask for images


def clone_from_git(git_url, output_folder):
    """
    Clone a git repository from a url.
    :param git_url: url of the git repository
    :param output_folder: path of the output folder
    :return: the cloned repository

    """
    # if the folder doesn't exist, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # the git repository has aleady been cloned
    try:
        repo = Repo.clone_from(git_url, output_folder)
    except GitCommandError:
        print("The repository has already been cloned")
        repo = Repo(output_folder) 
    return repo


# Function to clone branch from git to be made...


# function to ask for a directory
def ask_directory():
    """
    Ask for a directory
    :return: the path of the directory
    """
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    directory = askdirectory(initialdir=os.getcwd(),
                             title='Please select a directory')
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
    directory = askopenfilenames(
        initialdir=os.getcwd(), title='Please select a directory')
    # only keep image files
    images = []
    for image in directory:
        if image.endswith(".png") or image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith(".gif"):
            images.append(os.path.abspath(image))
    return images

# find file in tree


def find_file(path, filename):
    """
    Find a file in a tree and return the path of the file
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
    Find a folder in a tree and return the path of the folder
    :param path: the path of the tree
    :param foldername: the name of the folder
    :return: the path of the folder
    """
    for root, dirs, files in os.walk(path):
        if foldername in dirs:
            return os.path.abspath(os.path.join(root, foldername))
    return ""

# remove empty folders in tree recursively
def remove_empty_folders_recursively(path):
    """
    Remove empty folders in a tree recursively
    :param path: the path of the tree
    """
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if not os.listdir(os.path.join(root, dir)):
                os.rmdir(os.path.join(root, dir))
                remove_empty_folders_recursively(os.path.dirname(dir))
        if not os.listdir(root):
            os.rmdir(root)
    print("No more empty folders ! ")

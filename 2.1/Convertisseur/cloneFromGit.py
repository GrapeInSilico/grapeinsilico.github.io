import os
from git import Repo

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
import pypandoc
import os
import shutil
import random
from tkinter.filedialog import askopenfilenames, askdirectory
from tkinter import Tk

# Return the list of all the formats that are in the folder that we can convert
def see_all_convertible_format_folder(folder):
    """
    Return the list of all the formats that are in the folder that we can convert
    Args:
        folder: the folder
    type:
        folder: str
    """
    convertible = pypandoc.get_pandoc_formats()[0] # Files that we can convert | [1] : converted possible files type
    files = []
    for file in [os.path.join(folder, f) for f in os.listdir(folder)]:
        index_last_point = file.rfind('.')
        if (pypandoc.normalize_format(file[index_last_point+1:]) in convertible and file[index_last_point+1:] not in files):
            files.append(file[index_last_point+1:])
    return files

# Return the list of all the files that we can convert that are present in the folder
def see_all_convertible_files_folder(folder):
    """
    Return the list of all the files that we can convert that are present in the folder and a list of the files that we can't convert
    Args:
        folder: the folder
    type:
        folder: str
    """
    convertible = pypandoc.get_pandoc_formats()[0] + pypandoc.get_pandoc_formats()[1] # Files that we can convert | [1] : converted possible files type
    covertible_files = []
    not_convertible_files = []
    for file in [os.path.join(folder, f) for f in os.listdir(folder)]:
        index_last_point = file.rfind('.')
        if (pypandoc.normalize_format(file[index_last_point+1:]) in convertible):
            covertible_files.append(file)
        else:
            not_convertible_files.append(file)
    return [covertible_files, not_convertible_files]

# Convert a file with an olf format to a new format
# We suppose that the file is convertible
def convert_file(file, new_format, output_folder = os.getcwd()):
    # Get the format of the file
    old_format = os.path.basename(file).split('.')[-1]
    # Convert the file
    if (old_format == "ipynb" and new_format == "md"):
        os.system("jupyter nbconvert --to markdown " + file +" --output " + output_folder + "\\" + os.path.basename(file).replace(old_format, new_format))
    else:
        pypandoc.convert_file(file, format=old_format, to = new_format, outputfile= output_folder + "\\" + os.path.basename(file).replace(old_format, new_format))

# Convert a list of files by calling the function convert_file
# We suppose that all the files are convertible
def convert_files(files, new_format, output_folder = os.getcwd()):
    for file in files:
        convert_file(file, new_format, output_folder)

# Convert a folder by calling the function convert_files
# Create a new folder with the same base name as the old folder put in an output folder (only concerning the convertible files)
# Create a new folder with the same base name as the old folder put in an output folder (only concerning the convertible files)
def convert_folder(folder, new_format, output_folder_convertible = os.getcwd(), output_folder_not_convertible = os.getcwd()):
    new_output_folder_convertible = output_folder_convertible + "\\" + os.path.basename(folder)
    os.makedirs(new_output_folder_convertible, exist_ok=True)
    convert_files(see_all_convertible_files_folder(folder)[0], new_format, new_output_folder_convertible)
    for file in see_all_convertible_files_folder(folder)[1]:
        shutil.copy(file, output_folder_not_convertible)


convert_folder(r"C:\Users\gandeell\Documents\GitHub\grapeinsilico.github.io\2.1\Convertisseur\test", "md")



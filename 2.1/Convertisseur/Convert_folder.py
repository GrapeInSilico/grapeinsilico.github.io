import pypandoc
import os
import shutil
import random
from tkinter.filedialog import askopenfilenames, askdirectory
from tkinter import Tk

global rescue_foldername
rescue_foldername = r"C:\Users\gandeell\Documents\GitHub\grapeinsilico.github.io\2.1\test"
global i, posti, inde
i = 1
posti = 1
inde = 1

# get extension of a file
def get_extension(file):
    """
    Get extension of a file
    Args:
        file: the file
    type:
        file: str
"""
    index_last_point = file.rfind('.')
    return file[index_last_point+1:]

# ask for a list of files
def ask_files(copied_folder):
    """
    Ask for a list of files
    Args:
        copied_folder: the folder where the files and folders had been copied
    type:
        copied_folder: str
    """
    files = []
    folders = []
    answer = ""
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    while (answer != "done"):
        print("When you are done, enter 'done'")
        print("would you like to convert some files or a folder of files ?")
        answer = input("(1) files\n(2) folder\n")
        if answer == "1":
            print("Please select the files you want to convert")
            print("you can select multiple files by pressing ctrl+click")
            adress = askopenfilenames(initialdir=copied_folder, title="Select files")
            print()
            print("Files selected :")
            for file in adress:
                if (os.path.exists(file) and os.path.isfile(file)):
                    files.append(file)
            print(files)
            print()
        elif answer == "2":
            print("Please select the folders you want to convert")
            print("if you want to stop selecting folders, click on the cancel button")
            while True:
                adress = askdirectory(initialdir=copied_folder, title="Select folder")
                if (adress == ""):
                    break
                if (os.path.exists(adress) and os.path.isdir(adress)):
                    folders.append(adress)
            print()
            print("Folders selected :")
            print(folders)
            print()
        elif answer != "done" and answer != "1" and answer != "2":
            print("Please select a valid answer")
            ask_files()
    print("files = ", files)
    print("folders = ", folders)
    return [files, folders]

# convert the selected files and folers of ask_files()
def convert_files_and_folders(copied_folder, new_format, output_foldername="", image_folder=""):
    """
    Convert the selected files and folers of ask_files()
    Args:
        copied_folder: the folder where the files and folders are copied
        new_format: the format of the new files
        output_foldername: the folder where the new files will be saved
        image_folder: the folder where the images are saved
    type:
        copied_folder: str
        new_format: str
        output_foldername: str
        image_folder: str
    """
    list = ask_files(copied_folder)
    list_files = list[0]
    list_folders = list[1]
    for file in list_files:
        convert_file(file, get_extension(file), new_format, output_foldername, image_folder)
    for folder in list_folders:
        convert_tree(folder, new_format, output_foldername + "\\" + os.path.basename(folder), image_folder, convertible = False)

# get title of a markdown file
def get_title(file):
    """
    Get title of a markdown file
    Args:
        file: the file
    type:
        file: str
    """
    with open(file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                return line[2:].strip().replace("#", "").replace("_", " ").replace("`", " ")
    return ""

# list of all the images name in the folder
def list_images_folder(folder):
    """
    List of all the images name in the folder
    Args:
        folder: the folder
    type:
        folder: str
    """
    images = []
    for file in listdir_fullpath(folder):
        if (file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")):
            images.append(os.path.basename(file))
    return images

# List of all the files in the folder
def listdir_fullpath(d):
    """
    List of all the files in the folder
    Args:
        d: the folder
    type:
        d: str
    """
    return [os.path.join(d, f) for f in os.listdir(d)]

# import description if there is one
def import_description(file):
    """
    Import description if there is one
    Args:
        file: the file
    type:
        file: str
    """
    text= ""
    with open(file, 'r') as f:
        for line in f:
            #choose next line if it is a title
            if line.startswith('#') and line.find("Description") != -1:
                while line.strip() == "":
                    continue
                while line.strip() != "" and not line.startswith('#'):
                    text += line.strip
                    continue
                index_first_point = text.find('.')
                text = text[0:index_first_point]
                return text

    # return first three lines if there is no description
    with open(file, 'r') as f:
        k = 1
        for line in f:
            if line.startswith('#'):
                continue
            if line.strip() == "":
                continue
            if k > 3:
                break
            text += line.strip()
            k += 1
    return text

# import text from file from line a to line b
def import_text_from_file(file, a, b):
    """
    Import text from file from line a to line b
    Args:
        file: the file
        a: the first line
        b: the last line
    type:
        file: str
        a: int
        b: int
    """
    with open(file, 'r') as f:
        lines = f.readlines()
    text = ""
    for i in range(a, b):
        text += lines[i]
    return text

# import a text at the beginning of a file
def import_text(file, text):
    """
    Import a text at the beginning of a file
    Args:
        file: the file
        text: the text
    type:
        file: str
        text: str
    """
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file, 'w') as f:
        f.writelines(text + "\n")
        f.writelines(lines)

# We will convert the files of a folder each by each
def convert_file(file, old_format, file_format, output_foldername = "", image_folder_font_matter = ""):
    """
    Convert a file from old_format to file_format
    Args:
        file: the file
        old_format: the format of the file
        file_format: the format of the new file
        output_foldername: the folder where the new file will be saved
        image_folder_font_matter: the folder where the images are saved
    type:
        file: str
        old_format: str
        file_format: str
        output_foldername: str
        image_folder_font_matter: str
    """
    # Where 'output_filename' is the absolute path leading to the folder which will containe the converted file
    file = os.path.abspath(file)
    if output_foldername == "":
        output_foldername= os.path.dirname(file)
    elif not os.path.exists(output_foldername):
        os.makedirs(output_foldername)
    
    # First, the name of the output file is created 
    file_name = os.path.basename(file)
    index_last_point = file_name.rfind('.')
    new_file_name = output_foldername + "\\" +  file_name.replace(file_name[index_last_point:], '.' + file_format)
    
    # if new_file_name already exists, we will add a random number to the name
    if os.path.exists(new_file_name) :
        global i
        new_file_name = output_foldername + "\\" +  file_name.replace(file_name[index_last_point:], "(" + str(i) + ').' + file_format)
        i = i + 1

    # if the file is named index.md, we will rename it to index_i.md
    if os.path.basename(new_file_name) == "index.md":
        global inde
        new_file_name = output_foldername + "\\" +  "index_" + str(inde) + ".md"
        inde = inde + 1

    print()
    print("Converting : " + new_file_name)
    print()

    # Then the file is converted 
    try:
        print(file)
        if (os.path.splitext(file)[1] == ".ipynb"):
            output = os.system("jupyter nbconvert --to markdown " + os.path.abspath(file) +" --output " + output_foldername +"\\" + os.path.splitext(os.path.basename(file))[0] + ".md")
        else:
            output = pypandoc.convert_file(file, format=old_format, to =file_format, outputfile=new_file_name)
        print("File converted in " + output_foldername)
        if image_folder_font_matter != "":
            image = list_images_folder(image_folder_font_matter)
            images = "'\n"+ "image = 'images/post/"+image[random.randint(0, len(image)-1)] # Autimatically choose a random image from the folder (TO IMPROVE)
        else :
            images = ""
        # Title probleme to be fixed
        global posti
        string = "+++" +"\n" + "title = '" + get_title(new_file_name) + "'\n" + "slug = 'post"+ str(posti) + images +"'\n"+ "description = '" + import_description(new_file_name) +"'\n"+ "disableComments = true" +"\n" + "+++" +"\n"
        string.replace("'", "\"")
        posti = posti + 1
        import_text(new_file_name, string)
    except RuntimeError:
        print("bad format")
        global rescue_foldername
        # get parent folder of the folder
        rescue_foldername = os.path.dirname(output_foldername) + "\\" + "rescue"
        if not os.path.exists(rescue_foldername):
            os.makedirs(rescue_foldername)
        shutil.copy(file, os.path.abspath(rescue_foldername))
        print("Copied !")
    print()

# Call the function to convert the files of a list of files with a list of formats
def convert_multiple_files_with_formats(files, list_format, new_format, output_foldername="", image_folder=""):
    """
    Convert multiple files with different formats by calling the function convert_file
    Args:
        files: the list of files
        list_format: the list of formats - the same length as the list of files - to convert the files format by format
        new_format: the new format
        output_foldername: the folder where the new files will be saved
        image_folder: the folder where the images are saved
    type:
        files: list
        list_format: list
        new_format: str
        output_foldername: str
        image_folder: str
    """
    for format in list_format:
        for file in files:
            convert_file(file, format, new_format, output_foldername, image_folder)

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
    for file in listdir_fullpath(folder):
        index_last_point = file.rfind('.')
        if (pypandoc.normalize_format(file[index_last_point+1:]) in convertible and file[index_last_point+1:] not in files):
            files.append(file[index_last_point+1:])
    return files

# Return the list of all the files that we can convert that are present in the folder
def see_all_convertible_files_folder(folder):
    """
    Return the list of all the files that we can convert that are present in the folder
    Args:
        folder: the folder
    type:
        folder: str
    """
    convertible = pypandoc.get_pandoc_formats()[0] + pypandoc.get_pandoc_formats()[1] # Files that we can convert | [1] : converted possible files type
    files = []
    for file in listdir_fullpath(folder):
        index_last_point = file.rfind('.')
        if (pypandoc.normalize_format(file[index_last_point+1:]) in convertible):
            files.append(os.path.abspath(file))
    return files

# Convert only the compatible files of a folder with a new_format into an output_folder
def convert_folder_convertible(folder, new_format, output_foldername = "", image_folder=""):
    """
    Convert only the compatible files of a folder with a new_format into an output_folder
    Args:
        folder: the folder
        new_format: the new format
        output_foldername: the folder where the new files will be saved
        image_folder: the folder where the images are saved
    type:
        folder: str
        new_format: str
        output_foldername: str
        image_folder: str
    """
    if output_foldername == "":
        output_foldername = folder
    files = see_all_convertible_files_folder(folder)
    list_format = see_all_convertible_format_folder(folder)
    convert_multiple_files_with_formats(files, list_format, new_format, output_foldername, image_folder)

# Convert the compatible files (and copy the other ones) of a folder with a new_format into an output_folder
def convert_folder_all_included(folder, new_format, output_foldername = "", image_folder=""):
    """
    Convert the compatible files (and copy the other ones) of a folder with a new_format into an output_folder
    Args:
        folder: the folder
        new_format: the new format
        output_foldername: the folder where the new files will be saved
        image_folder: the folder where the images are saved
    type:
        folder: str
        new_format: str
        output_foldername: str
        image_folder: str
    """
    if output_foldername == "":
        output_foldername = folder
    files = see_all_convertible_files_folder(folder)
    list_format = see_all_convertible_format_folder(folder)
    for file in listdir_fullpath(folder):
        if (file not in files and os.path.isfile(file)):
            shutil.copy(file, os.path.abspath(output_foldername))
    convert_multiple_files_with_formats(files, list_format, new_format, output_foldername, image_folder)

# Replicate and convert somes files in an entirey tree of folders (all of them if convertible == False, only the convertible if convertible == True)
def convert_tree(folder, new_format, output_foldername = "", image_folder = "", convertible = False):
    """
    Replicate and convert somes files in an entirey tree of folders (all of them if convertible == False, only the convertible if convertible == True)
    Args:
        folder: the folder
        new_format: the new format
        output_foldername: the folder where the new files will be saved
        image_folder: the folder where the images are saved
        convertible: if we want to convert only the convertible files or all of them
    type:
        folder: str
        new_format: str
        output_foldername: str
        image_folder: str
        convertible: bool
    """
    if output_foldername == "":
        output_foldername = folder
    
    if not os.path.exists(output_foldername):
        os.mkdir(output_foldername)

    if convertible:
        convert_folder_convertible(folder, new_format, output_foldername, image_folder)
    else:
        convert_folder_all_included(folder, new_format, output_foldername, image_folder)

    for object in listdir_fullpath(folder):
        if os.path.isdir(object):
            try:
                print("new folder : "+os.path.abspath(output_foldername) + "\\" + os.path.basename(object))
                os.mkdir(os.path.abspath(output_foldername) + "\\" + os.path.basename(object))
            except FileExistsError:
                print("Folder already exists")
            convert_tree(object, new_format, os.path.abspath(output_foldername) + "\\" + os.path.basename(object), image_folder)

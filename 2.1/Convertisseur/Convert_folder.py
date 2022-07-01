import pypandoc
import os
import shutil
import random


# get title of a markdown file
def get_title(file):
    with open(file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                return line[2:].strip()
    return ""

# get first sentence after the title of a markdown file
def get_first_sentence(file):
    with open(file, 'r') as f:
        for line in f:
            #choose next line if it is a title
            if line.startswith('#'):
                continue
            #choose next line if it is a empty line
            if line.strip() == "":
                continue
            #return the first sentence
            else:
                return line.strip().replace("#", "").replace("_", " ").replace("`", " ")
    return ""

# list of all the images name in the folder
def list_images_folder(folder):
    images = []
    for file in listdir_fullpath(folder):
        if (file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")):
            images.append(os.path.basename(file))
    return images

# List of all the files in the folder
def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

# import a text at the beginning of a file
def import_text(file, text):
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file, 'w') as f:
        f.writelines(text + "\n")
        f.writelines(lines)

# We will convert the files of a folder each by each

def convert_file(file, old_format, file_format, output_foldername = ""): 
    # Where 'output_filename' is the absolute path leading to the folder which will containe the converted file
    file = os.path.abspath(file)
    if output_foldername == "":
        output_foldername= os.path.dirname(file)
    
    # First, the name of the output file is created 
    file_name = os.path.basename(file)
    index_last_point = file_name.rfind('.')
    new_file_name = output_foldername + "\\" + file_name.replace(file_name[index_last_point:], '.' + file_format)

    # Then the file is converted 
    try:
        print(file)
        if (os.path.splitext(file)[1] == ".ipynb"):
            output = os.system("jupyter nbconvert --to markdown " + os.path.abspath(file) +" --output " + output_foldername +"\\" + os.path.splitext(os.path.basename(file))[0] + ".md")
        else:
            output = pypandoc.convert_file(file, format=old_format, to =file_format, outputfile=new_file_name)
        #assert output == "", "Ouch problem"
        print("File converted in " + output_foldername)
        images = list_images_folder(r"C:\Users\gandeell\Documents\GitHub\grapeinsilico.github.io\2.1\test\hugo_test_2_1\static\images\test")
        # Title probleme to be fixed
        string = "+++" +"\n" + "title = '" + get_title(output_foldername +"\\" + os.path.splitext(os.path.basename(file))[0] + ".md") + "'\n" + "slug = 'post"+ str(random.randint(0,100)) +"'\n"+ "image = 'images/test/"+images[random.randint(0, len(images)-1)] +"'\n"+ "description = '" + get_first_sentence(file) +"'\n"+ "disableComments = true" +"\n" + "+++" +"\n"
        string.replace("'", "\"")
        import_text(new_file_name, string)
    except RuntimeError:
        print("bad format")
        shutil.copy(file, os.path.abspath(output_foldername))
        print("Copied !")
    print()

# Call the function to convert the files of a list of files with a list of formats
def convert_multiple_files_with_formats(files, list_format, new_format, output_foldername):
    for format in list_format:
        for file in files:
            convert_file(file, format, new_format, output_foldername)

# Return the list of all the formats that are in the folder that we can convert
def see_all_convertible_format_folder(folder):
    convertible = pypandoc.get_pandoc_formats()[0] # Files that we can convert | [1] : converted possible files type
    files = []
    for file in listdir_fullpath(folder):
        index_last_point = file.rfind('.')
        if (pypandoc.normalize_format(file[index_last_point+1:]) in convertible and file[index_last_point+1:] not in files):
            files.append(file[index_last_point+1:])
    return files

# Return the list of all the files that we can convert that are present in the folder
def see_all_convertible_files_folder(folder):
    convertible = pypandoc.get_pandoc_formats()[0] + pypandoc.get_pandoc_formats()[1] # Files that we can convert | [1] : converted possible files type
    files = []
    for file in listdir_fullpath(folder):
        index_last_point = file.rfind('.')
        if (pypandoc.normalize_format(file[index_last_point+1:]) in convertible):
            files.append(os.path.abspath(file))
    return files

# Convert only the compatible files of a folder with a new_format into an output_folder
def convert_folder_convertible(folder, new_format, output_foldername = ""):
    if output_foldername == "":
        output_foldername = folder
    files = see_all_convertible_files_folder(folder)
    list_format = see_all_convertible_format_folder(folder)
    convert_multiple_files_with_formats(files, list_format, new_format, output_foldername)

# Convert the compatible files (and copy the other ones) of a folder with a new_format into an output_folder
def convert_folder_all_included(folder, new_format, output_foldername = ""):
    if output_foldername == "":
        output_foldername = folder
    files = see_all_convertible_files_folder(folder)
    list_format = see_all_convertible_format_folder(folder)
    for file in listdir_fullpath(folder):
        if (file not in files and os.path.isfile(file)):
            shutil.copy(file, os.path.abspath(output_foldername))
    convert_multiple_files_with_formats(files, list_format, new_format, output_foldername)


folder = r"C:\Users\gandeell\Documents\pandoc-test\test\Repo\doc"
files = see_all_convertible_files_folder(folder)
list_format = see_all_convertible_format_folder(folder)
new_format = "md"
output_foldername = r"C:\Users\gandeell\Documents\pandoc-test\test\Copied"

#convert_folder_all_included(folder, new_format, output_foldername)

folder = r"C:\Users\gandeell\Documents\pandoc-test\test\Repo\example"
files = see_all_convertible_files_folder(folder)
list_format = see_all_convertible_format_folder(folder)
new_format = "md"
output_foldername = r"C:\Users\gandeell\Documents\pandoc-test\test\Copied"

#convert_multiple_files_with_formats(files, list_format, new_format, output_foldername)


# Replicate and convert somes files in an entirey tree of folders (all of them if convertible == False, only the convertible if convertible == True)
def convert_tree(folder, new_format, output_foldername = "", convertible = False, First_run = True):

    if First_run:
        if output_foldername == "":
            output_foldername = folder
        else:
            output_foldername = output_foldername + "\\"+ os.path.basename(folder) + "_converted"
    else:
        if output_foldername == "":
            output_foldername = folder + "\\"+ os.path.basename(folder) + "_converted"
        else:
            output_foldername = output_foldername 
    
    if not os.path.exists(output_foldername):
        os.mkdir(output_foldername)

    if convertible:
        convert_folder_convertible(folder, new_format, output_foldername)
    else:
        convert_folder_all_included(folder, new_format, output_foldername)

    for object in listdir_fullpath(folder):
        if os.path.isdir(object):
            try:
                print("new folder : "+os.path.abspath(output_foldername) + "\\" + os.path.basename(object))
                os.mkdir(os.path.abspath(output_foldername) + "\\" + os.path.basename(object))
            except FileExistsError:
                print("Folder already exists")
            convert_tree(object, new_format, os.path.abspath(output_foldername) + "\\" + os.path.basename(object), First_run=False)

print()
print("start---------------------------------------")
print()

folder = r"C:\Users\gandeell\Documents\pandoc-test\test\Repo"
files = see_all_convertible_files_folder(folder)
list_format = see_all_convertible_format_folder(folder)
new_format = "md"
output_foldername = r"C:\Users\gandeell\Documents\GitHub\grapeinsilico.github.io\2.1\test\hugo_test_2_1\content\post"

convert_tree(folder, new_format, output_foldername)

#convert_folder_convertible(r"C:\Users\gandeell\Documents\pandoc-test\test\Repo\example", "md", r"C:\Users\gandeell\Documents\GitHub\grapeinsilico.github.io\2.1\test\hugo_test_2_1\content\post")


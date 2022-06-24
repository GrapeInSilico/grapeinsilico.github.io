import pypandoc
import os
import shutil

# List of all the files in the folder
def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


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
        output = pypandoc.convert_file(file, format=old_format, to =file_format, outputfile=new_file_name)
        assert output == "", "Ouch problem"
        print("File converted in " + output_foldername)
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
    convertible = pypandoc.get_pandoc_formats()[0] # Files that we can convert | [1] : converted possible files type
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
new_format = "rst"
output_foldername = r"C:\Users\gandeell\Documents\pandoc-test\test\Copied"

convert_tree(folder, new_format, output_foldername)



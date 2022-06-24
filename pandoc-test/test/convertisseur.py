import pypandoc
import os

# Function to convert file to another format using pandoc
def convert_file(file, file_format):
    #First, the name of the output file is created 
    index_last_point = file.rfind('.')
    output_filename = file.replace(file[index_last_point:], '.' + file_format)
    print("output_filename: " + output_filename)
    # Then the file is converted 
    output = pypandoc.convert_file(file, file_format, outputfile=output_filename)
    assert output == "", "Error converting file -> check the pandoc compatibility"
    print("File converted")
    print()

convert_file(r"C:\Users\gandeell\Documents\test\readme.md", "rst")
convert_file(r"C:\Users\gandeell\Documents\test\readme.md", "html")

# Function to convert file to another format using pandoc but with a different name (No extension)
def convert_file_with_name(file, file_format, output_filename):
    # First, the name of the output file is created 
    new_file_name = output_filename
    print("output_filename: " + new_file_name)
    # Then the file is converted 
    try:
        output = pypandoc.convert_file(file, file_format, outputfile=new_file_name)
        assert output == "", "Error converting file -> check the pandoc compatibility"
        print("File converted")
    except RuntimeError:
        print("bad format")
    print()

convert_file_with_name("readme.md", "rst", "jeandamien")
convert_file_with_name(r"C:\Users\gandeell\Documents\test\readme.md", "rst", r"C:\Users\gandeell\Documents\test\Fichier rst\readme")

def convert_files(files, file_format):
    for file in files:
        convert_file(file, file_format)
    return files

def convert_files_with_name(files, file_format, output_filenames):
    for i in range(len(files)):
        convert_file_with_name(files[i], file_format, output_filenames[i])
    return files

# convert files in a folder
def convert_files_in_folder(folder, file_format):
    files = []
    for file in os.listdir(folder):
        files.append(folder + "\\" + file)
    convert_files(files, file_format)

convert_files_in_folder(r"C:\Users\gandeell\Documents\test\Raoult", 'md')

# convert files in a folder and save them in a different folder
def convert_files_in_new_folder(folder, file_format, output_folder):
    files = []
    output_files = []
    for file in os.listdir(folder):
        index_last_point = file.rfind('.')
        files.append(folder + "\\" + file)
        output_files.append(output_folder + "\\" + file.replace(file[index_last_point:], '.' + file_format))
    convert_files_with_name(files, file_format, output_files)



convert_files_in_new_folder(r"C:\Users\gandeell\Documents\test\Raoult", 'md', r"C:\Users\gandeell\Documents\test\R3")

convert_files_in_new_folder(r"C:\Users\gandeell\Documents\test\Repo", "md", r"C:\Users\gandeell\Documents\test\R2")


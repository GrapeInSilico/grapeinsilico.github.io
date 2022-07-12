import pypandoc
import os
import shutil
import write

global image_base, list_folder_to_rewrite
list_folder_to_rewrite = []
image_base = os.getcwd()

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
    Return the list of all the files that we can convert that are present in the folder, along with lists of files that we can't convert such as images and folders
    Args:
        folder: the folder
    type:
        folder: str
    """
    convertible = pypandoc.get_pandoc_formats()[0] + pypandoc.get_pandoc_formats()[1] # Files that we can convert | [1] : converted possible files type
    covertible_files = []
    not_convertible_files_images = []
    not_convertible_files_other = []
    fold = []
    for file in [os.path.join(folder, f) for f in os.listdir(folder)]:
        index_last_point = file.rfind('.')
        if (pypandoc.normalize_format(file[index_last_point+1:]) in convertible):
            covertible_files.append(file)
        elif (os.path.isfile(file)):
            # if the file is an image
            if (file[index_last_point+1:] == "png" or file[index_last_point+1:] == "jpg" or file[index_last_point+1:] == "jpeg" or file[index_last_point+1:] == "gif"):
                not_convertible_files_images.append(file)
            else:
                not_convertible_files_other.append(file)
        else:
            fold.append(file)
    return [covertible_files, not_convertible_files_images, not_convertible_files_other, fold]

# Convert a file with an olf format to a new format
# We suppose that the file is convertible
def convert_file(file, new_format, output_folder = os.getcwd()):
    """
    Convert a file with an old format to a new format
    Also rewrite the file if it is a markdown file 
    Args:
        file: the file
        new_format: the new format
        output_folder: the folder where the file will be saved
    type:
        file: str
        new_format: str
        output_folder: str
    """
    # Get the format of the file
    old_format = os.path.basename(file).split('.')[-1]
    # Convert the file
    new_file = output_folder + "\\" + os.path.basename(file).replace(old_format, new_format)
    print("Converting " + file + " to " + new_file)
    if (old_format == "ipynb" and new_format == "md"):
        os.system("jupyter nbconvert --to markdown " + file +" --output " + new_file)
    else:
        pypandoc.convert_file(file, format=old_format, to = new_format, outputfile= new_file)
    # Write the file above the converted file
    write.write_above(new_file, write.generate_text(new_file))
    # Rename the file if needed (case index.md file)
    new_file = write.rename(new_file)
    # Adapting the file if it contains images (rewritte the image path)
    detection = write.detect_image_in_file(new_file)
    if (detection[0]):
        list_folder_to_rewrite.append(new_file)

# Convert a list of files by calling the function convert_file
# We suppose that all the files are convertible
def convert_files(files, new_format, output_folder = os.getcwd()):
    """
    Convert a list of files by calling the function convert_file
    Args:
        files: the list of files
        new_format: the new format
        output_folder: the folder where the files will be saved
    type:
        files: list
        new_format: str
        output_folder: str
    """
    for file in files:
        convert_file(file, new_format, output_folder)

# Copy a list of files (not convertible) to a folder
def copy_files(files, output_folder = os.getcwd()):
    """
    Copy a list of files (not convertible) to a folder
    Args:
        files: the list of files
        output_folder: the folder where the files will be saved
    type:
        files: list
        output_folder: str
    """
    for file in files:
        shutil.copy(file, output_folder)

# Convert a folder (and its tree) to a new format
def convert_folder(folder, new_format, output_folder = os.getcwd()):
    """
    Convert a folder (and its tree) to a new format
    Args:
        folder: the folder
        new_format: the new format
        output_folder: the folder where the folder will be saved
    type:
        folder: str
        new_format: str
        output_folder: str
    """
    # Create the folder if it doesn't exist
    output_folder = output_folder + "\\" + os.path.basename(folder)
    os.makedirs(output_folder, exist_ok=True)
    # Convert all the files in the folder in the new folder
    files = see_all_convertible_files_folder(folder)
    convert_files(files[0], new_format, output_folder)
    copy_files(files[1], output_folder)
    copy_files(files[2], output_folder)
    # Convert all the folders in the folder in the new folder
    for subfolder in files[3]:
        convert_folder(subfolder, new_format, output_folder)

# Convert a folder (and its tree) to a new format
# The output folder is adapted to hugo tree structure
def convert_folder_2_Hwebsite(folder, new_format, website = os.getcwd(), part_of_website = "", all_as_posts = False):
    """
    Convert a folder (and its tree) to a new format and adapt the output folder to hugo tree structure
    Args:
        folder: the folder
        new_format: the new format
        website: the website
        part_of_website: the part of the website
        all_as_posts: if all the files in the folder are converted as posts
    type:
        folder: str
        new_format: str
        website: str
        part_of_website: str
        all_as_posts: bool
    """
    global image_base
    image_base =  website + "\\static\\images\\"
    if (not all_as_posts):
        # Folder containing all the markdown files and subfolders (example : part_of_website = "post")
        content_folder = website + "\\content" + "\\" + part_of_website + "\\" + os.path.basename(folder)
        # Image linked to the content (used in it)
        image_folder = website + "\\static\\images" + "\\" + part_of_website + "\\" + os.path.basename(folder)
        # object linked to the content (used in it)
        orther_static_folder = website + "\\static\\other" + "\\" + part_of_website + "\\" +  os.path.basename(folder)
    else:
        # Folder containing all the markdown files and subfolders (example : part_of_website = "post")
        content_folder = website + "\\content" + "\\post" 
        # Image linked to the content (used in it)
        image_folder = website + "\\static\\images" + "\\" + part_of_website + "\\" + os.path.basename(folder)
        # object linked to the content (used in it)
        orther_static_folder = website + "\\static\\other"+ "\\" + part_of_website + "\\" + os.path.basename(folder)
    print("content_folder = ",content_folder)
    
    # Create these folders if they don't exist
    os.makedirs(content_folder, exist_ok=True)
    os.makedirs(image_folder, exist_ok=True)
    os.makedirs(orther_static_folder, exist_ok=True)
    # Convert all the files in the folder in the new folder
    files = see_all_convertible_files_folder(folder)
    convert_files(files[0], new_format, content_folder)
    copy_files(files[1], image_folder)
    copy_files(files[2], orther_static_folder)
    # Convert all the folders in the folder in the new folder
    part_of_website = part_of_website + "\\" + os.path.basename(folder)
    for subfolder in files[3]:
        convert_folder_2_Hwebsite(subfolder, new_format, website, part_of_website, all_as_posts)

import cloneFromGit
url_git = "https://github.com/openalea/openalea.rtfd.io"
path_content = r"C:\Users\gandeell\Documents\GitHub\grapeinsilico.github.io\2.1\Convertisseur\post"
to_Format = "md"
output_website = r"C:\Users\gandeell\Documents\GitHub\grapeinsilico.github.io\warudo"
cloneFromGit.clone_from_git(url_git, path_content)
convert_folder_2_Hwebsite(path_content, to_Format, output_website , all_as_posts=False)

for file in list_folder_to_rewrite:
    write.rewrite_images(file, file, image_base)
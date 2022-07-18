import os
from difflib import get_close_matches


global i, inde
i = 0
inde = 0

# renaming file if needed
def rename(file):
    """
    Renaming file if needed
    Args:
        file: the file
    type:
        file: str
    """
    # if file name == index.md, add 1 to the index
    if os.path.basename(file) == "index.md":
        global inde
        inde += 1
        # change the name of the file
        os.rename(file, os.path.dirname(file) + "\\" + os.path.basename(file).split('/')[-1].split('.')[0] + str(inde) + ".md")
        return os.path.dirname(file) + "\\" + os.path.basename(file).split('/')[-1].split('.')[0] + str(inde) + ".md"
    return file

# write text at the begining of a file
def write_above(file, text):
    """
    Write text at the begining of a file
    Args:
        file: the file
        text: the text to write
    type:
        file: str
        text: str
    """
    with open(file, "r") as f:
        lines = f.readlines()
    with open(file, "w") as f:
        f.write(text)
        f.writelines(lines)
    return

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
                return line[2:].strip().replace("\n", " ").replace("#", "").replace("_", " ").replace("`", " ").replace("'"," ")
    # return file name if there is no title
    return os.path.basename(file).split('/')[-1].split('.')[0]

# import description if there is one
def import_description(file):
    """
    Import description if there is one
    If there is no description, return the first sentence of the file
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
                return text.replace("\n", " ").replace("#", "").replace("`", " ").replace("'"," ")

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
    return text.replace("\n", " ").replace("#", "").replace("`", " ").replace("'"," ")

# generate the text to write at the begining of a file
def generate_text(file, extension_config):
    """
    Generate the text to write at the begining of a file (font matter: title, description)
    Args:
        file: the file
    type:
        file: str
    """
    global i
    i += 1
    if (extension_config == "toml"):
        text = "+++" + "\n" + "title ='" + get_title(file) + "'\n"
        # Image part yet missing
        text += "slug = 'post" + str(i) + "'\n"
        text += "description = '" + import_description(file) +"'\n" + "disableComments = true\n"
        text = text + "+++" + "\n\n"
    else: # extension_config == "yaml"
        text = "---\n" + "title: '" + get_title(file) + "'\n"
        # Image part yet missing
        text += "slug: 'post" + str(i) + "'\n"
        text += "description: '" + import_description(file) + "'\n" + "disableComments: 'true'\n"
        text = text + "---\n\n"
    return text

# detect image in a markdown file
def detect_image_in_file(file):
    """
    Detect image in a markdown file and give the link of the image
    Args:
        file: the file
    type:
        file: str
    """
    with open(file, 'r') as f:
        bool = False
        begin_path = []
        for line in f:
            # the first 'or' statement is to avoid detecting images as description (line jumping - pandoc bug)
            if (line.startswith('![') or line.find(']') != -1) and (line.find('png') != -1 or line.find('jpg') != -1 or line.find('jpeg') != -1 or line.find('gif') != -1):
                bool = True
                if line.find("(./") != -1 and ("(./" not in begin_path):
                    begin_path.append("(./")
                elif line.find("(/") != -1 and ("(/" not in begin_path):
                    begin_path.append("(/")
                elif line.find("(") != -1 and ("(" not in begin_path):
                    begin_path.append("(")
    return [bool, begin_path]


# search a file in all the subdirectories of a directory
def search_file_path(root, partial_path, old_file_path):
    """
    Search a file with its partial path in all the subdirectories of a directory
    As a last resort, search the most "matching file" in the subdirectories
    Return part of the path of the path the file needed for markdown imports
    Args:
        root: the root
        file: the file
    type:
        root: str
        file: str
    """
    dirname = os.path.normpath(os.path.dirname(partial_path))
    list_name = [] 
    for root, dirs, files in os.walk(root):
        if dirname in root:
            list_name.append(root)
    if len(list_name) == 1:
        im = list_name[0].replace("\\", "/").find("/images/")
        return list_name[0].replace("\\", "/")[im:] + "/" + os.path.basename(partial_path)
    elif len(list_name) > 1: # if there is more than one directory with the same name
        # see the common part of the path between the file we want to find and the old path of the converted file 
        im = get_close_matches(old_file_path, list_name, n=1, cutoff=0.8)[0].replace("\\", "/").find("/images/") 
        return get_close_matches(old_file_path, list_name, n=1, cutoff=0.8)[0].replace("\\", "/")[im:] + "/" + os.path.basename(partial_path)
    return os.getcwd()

# get link of an image from a markdown file
def get_partial_path(file):
    """
    Get link of an image from a markdown file
    Args:
        file: the file
    type:
        file: str
    """
    line_and_numbers = []
    with open(file, 'r') as f:
        number = 0
        for line in f:
            if (line.startswith('![') or line.find(']')) != -1 and (line.find('png') != -1 or line.find('jpg') != -1 or line.find('jpeg') != -1 or line.find('gif') != -1):
                parenthesis_1 = line.find('(')
                parenthesis_2 = line.find(')')
                line_and_numbers.append([line.strip()[parenthesis_1+1:parenthesis_2], number])
            number += 1
    return line_and_numbers

def rewrite_images(file, old_file_path, image_path):
    """
    Rewrite a file
    Args:
        file: the file
        text: the text to write
    type:
        file: str
        text: str
    """
    for element in get_partial_path(file):
        old_link = element[0]
        line_number = element[1]
        # replace line with its number
        with open(file, 'r') as f:
            lines = f.readlines()
            lines[line_number] = lines[line_number].replace(old_link, search_file_path(image_path, old_link, old_file_path))
        with open(file, 'w', encoding='utf-8') as f:
            f.writelines(lines)



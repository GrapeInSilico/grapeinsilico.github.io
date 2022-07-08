import fileinput
import sys
import os


global i, inde
i = 0
inde = 0

# renaming file if needed
def rename(file):
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
                return text.replace("\n", " ").replace("#", "").replace("_", " ").replace("`", " ").replace("'"," ")

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
    return text.replace("\n", " ").replace("#", "").replace("_", " ").replace("`", " ").replace("'"," ")

# generate the text to write at the begining of a file
def generate_text(file):    
    global i
    i += 1
    text = "+++" + "\n" + "title ='" + get_title(file) + "'\n"
    # Image part yet missing
    text += "slug = 'post" + str(i) + "'\n"
    text += "description = '" + import_description(file) +"'\n" + "disableComments = true\n"
    text = text + "+++" + "\n\n"
    return text

# detect image in a markdown file
def detect_image(file):
    """
    Detect image in a markdown file
    Args:
        file: the file
    type:
        file: str
    """
    with open(file, 'r') as f:
        for line in f:
            if line.startswith('![') and line.find(']') != -1 and (line.find('png') != -1 or line.find('jpg') != -1 or line.find('jpeg') != -1 or line.find('gif') != -1):
                return True
    return False

def rewrite(file, previousw, nextw):
   for line in fileinput.input(file, inplace=1):
        if line.startswith('![') and line.find(']') != -1 and (line.find('png') != -1 or line.find('jpg') != -1 or line.find('jpeg') != -1 or line.find('gif') != -1):
            line = line.replace(previousw, nextw)
        sys.stdout.write(line)

import os
import shutil
import subprocess

import cloneFromGit
import Conversion

print()

print("First step: Download Go : https://go.dev/dl/")

print()

print("Second step: Download goHugo : https://github.com/gohugoio/hugo/releases (we recommand the extended version)")
print("Then add it to your PATH variable (environnment variable)")


print()

print("Third step: Creating a new website")
print("Where would you like to create your website?")
site_folder = os.path.abspath(cloneFromGit.ask_directory())
print("Your website will be created in " + site_folder)
name = input("Give it a name (ex: my_website) \n")
os.system("cd " + site_folder + " && hugo new site " + name)
print()

print("Fourth step: clone your gitHub repository :")

git_url = []

url = ""
# get the input from the user
while url != "done":
    url = input("Please enter the url of your repositories : ")
    git_url.append(url)
    print("The url has been added to the list")
    print("enter 'done' to finish")
    print("...")
git_url.remove("done")

if git_url == [] or git_url == [""]:
    git_url.append(r"https://github.com/openalea/openalea.rtfd.io")

clone_folder = []
i=0
# clone each repository
for git in git_url:
    # get the name of the URL
    git_name = git.split("/")[-1]
    # get directory of the current file
    clone_folder.append(os.path.dirname(os.path.realpath(__file__)) + "\\" + git_name)
    # copy git repo in the current directory
    cloneFromGit.clone_from_git(git, clone_folder[i])
    #cloneFromGit.clone_branch(git, "test-Loaï", clone_folder[i])
    i += 1

print()
print("Fifth step: choose the theme that you want to use : https://themes.gohugo.io/")
theme_url = input("Please return its git repository, for example : https://github.com/CaiJimmy/hugo-theme-stack \n")
subprocess.call("cd " + site_folder + "\\" + name + "&& git init && git submodule add " + theme_url + " themes/" + theme_url.split("/")[-1], shell=True)

print("Select the images you want to use in your website")
image_list = cloneFromGit.ask_images()
image_folder = site_folder + "\\" + name + "\\" + "static\\" + "images"
os.makedirs(image_folder + "\\" + "post")
for image in image_list:
    shutil.copy(image, image_folder + "\\post\\" + os.path.basename(image))

print()
print("Configuring config.toml")
# Copy the config.toml file in a string
config_toml_string = open(site_folder + "\\" + name + "\\" + "config.toml", "r").read() + "\n"
print(config_toml_string)
os.remove(site_folder + "\\" + name + "\\" + "config.toml")

try:
    shutil.copytree(cloneFromGit.find_folder(site_folder + "\\" + name +"\\" + "themes/" + theme_url.split("/")[-1] + "\\" + "exampleSite", "config"), site_folder + "\\" + name + "\\" + "config")
except FileNotFoundError:
    try:
        print("No config folder found")
        shutil.copyfile(cloneFromGit.find_file(site_folder + "\\" + name +"\\" + "themes/" + theme_url.split("/")[-1] + "\\" + "exampleSite", "config.toml"), site_folder + "\\" + name + "\\" + "config.toml")
        #cloneFromGit.change_line(site_folder + "\\" + name + "\\" + "config.toml", "theme = ", "theme = '" + theme_url.split("/")[-1] + "'\n")
        Conversion.extension_config = "toml"
    except FileNotFoundError:
        try:
            print("No config.toml folder found")
            shutil.copyfile(cloneFromGit.find_file(site_folder + "\\" + name +"\\" + "themes/" + theme_url.split("/")[-1] + "\\" + "exampleSite", "config.yaml"), site_folder + "\\" + name + "\\" + "config.yaml")
            #cloneFromGit.change_line(site_folder + "\\" + name + "\\" + "config.toml", "theme = ", "theme = '" + theme_url.split("/")[-1] + "'\n")
            Conversion.extension_config = "yaml"
        except FileNotFoundError:
            print("No config.yaml file found")
            # write sentence at the end of the file
            os.makedirs(site_folder + "\\" + name + "\\" + "config.toml")
            with open(site_folder + "\\" + name + "\\" + "config.toml", "a") as myfile:
                myfile.write(config_toml_string + "theme = '"+theme_url.split("/")[-1]+"'")


print()
print("start---------------------------------------")
print()

for c_f in clone_folder:
    print("Converting the folder : " + c_f)
    new_format = "md"

    Conversion.convert_folder_2_Hwebsite(c_f, new_format, site_folder + "\\" + name, part_of_website = "", all_as_posts = True)
    Conversion.adapt_images()




print()
print("lets see the website :")
#import webbrowser
#webbrowser.open('http://localhost:1313/')

#for fold in clone_folder:
 #   shutil.rmtree(fold)

print()
print("Done ! You can now see your website ")
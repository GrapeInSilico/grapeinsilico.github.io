import cloneFromGit
import Convert_folder

git_url = r"https://github.com/openalea/openalea.rtfd.io"
clone_folder = r"C:\Users\gandeell\Documents\GitHub\grapeinsilico.github.io\2.1\Convertisseur\openalea"
 
cloneFromGit.clone_from_git(git_url, clone_folder)

print()
print("start---------------------------------------")
print()

files = Convert_folder.see_all_convertible_files_folder(clone_folder)
list_format = Convert_folder.see_all_convertible_format_folder(clone_folder)
new_format = "md"
output_foldername = r"C:\Users\gandeell\Documents\GitHub\grapeinsilico.github.io\2.1\test\hugo_massive\content\post"
image_folder = r"C:\Users\gandeell\Documents\GitHub\grapeinsilico.github.io\2.1\test\hugo_massive\static\images\post"

Convert_folder.convert_files_and_folders(clone_folder, new_format, output_foldername, image_folder)
# Python program to explain shutil.copytree() method
		
# importing os module
import os
	
# importing shutil module
import shutil
	

def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]

# path
path = os.getcwd()
	
# List files and directories
# in 'C:/Users / Rajnish / Desktop / GeeksforGeeks'
print("Before copying file:")
print(os.listdir(path))
	
	
# Source path
src = r'C:\Users\gandeell\Documents\test\Repo'
	
# Destination path
R2 = r'C:\Users\gandeell\Documents\test\R2'
	
# Copy the content of
# source to destination
# using shutil.copy() as parameter
destination = shutil.copytree(src, R2, copy_function = shutil.copy, ignore=ignore_files)
	
# List files and directories
# in "C:/Users / Rajnish / Desktop / GeeksforGeeks"
print("After copying file:")
print(os.listdir(path))
	
# Print path of newly
# created file
print("Destination path:", destination)

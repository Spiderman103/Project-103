import os 
import shutil

from_dir = "C:/Users/sahil/OneDrive/Documents/C-102 Project - BYJU"
to_dir = "C:/Users/sahil/OneDrive/Desktop"

list_of_files = os.listdir(from_dir)
#print(list_of_files)


for i in list_of_files:
    os.path.splitext(list_of_files)


path1 = from_dir + "/" + filename
path2 = to_dir + "/" + "Document_Files"
path3 = to_dir + "/" + "Document_Files" + "/" + filename


if os.path.exiss(path2):
    print("Moving "+ file_name + ".....")


    shutil.move(path1,path3)   

else: 
    os.makedirs(path2)
    print("Moving " + file_name + "....." )
    shutil.move(path1,path3) 



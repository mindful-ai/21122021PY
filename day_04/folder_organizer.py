import os
import os.path
import shutil

path = r"C:\Users\Purushotham\Desktop\oralcepy\day_04\mydir"
os.chdir(path)

exts = [os.path.splitext(f)[1][1:] for f in os.listdir()]
for ext in set(exts):
    os.mkdir(ext)

for file in os.listdir():
    if(os.path.isfile(file)):
        target = os.path.join(os.getcwd(),os.path.splitext(file)[1][1:])
        shutil.move(file, target)
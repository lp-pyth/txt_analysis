import os
from os import path
import shutil


src = r"C:\PATH"
dst = r"C:\PATH\NEW"

filenames=['00001', '00003']

for k in range(len(filenames)):
    files = [i for i in os.listdir(src) if i.startswith(filenames[k]) and path.isfile(path.join(src, i))]

    for f in files:
        shutil.move(path.join(src, f), dst)
  
import pyperclip
import os
import shutil
import subprocess
import send2trash
from datetime import date
import re

copied_path = pyperclip.paste()


def start():
    os.chdir(copied_path)
    name_change()
    making_dirs()
    files_segregation()

def name_change():
    regPattern = re.compile(r'\d\d\d\d-.*')
    mo = regPattern.search(copied_path)
    newFileName = mo.group()
    fileName = newFileName
    file_numbering = 1
    for f in os.listdir(copied_path):
        extension = os.path.splitext(f)[1]
        os.rename(f,fileName + '-' + str(file_numbering) + extension.lower())
        file_numbering += 1
    
def making_dirs():
    os.makedirs(copied_path + '\\1920')
    os.makedirs(copied_path + '\\Hires')
    os.makedirs(copied_path + '\\Files')
    os.makedirs(copied_path + '\\Opis')


def files_segregation():
    for f in os.listdir(copied_path):
        extension = os.path.splitext(f)[1]
        if os.path.isfile(f):
            if extension == '.jpg' or extension == '.png' or extension == '.tif':
                shutil.move(f,copied_path + '\\Hires')
            elif extension == '.docx' or extension == '.txt' or extension == '.doc':
                shutil.move(f,copied_path + '\\Opis')
            else:
                shutil.move(f,copied_path + '\\Files')
        else:
            photoshop_action()

def photoshop_action():
    os.chdir(copied_path + '\\Hires')
    photoshop_path = ('C:\Program Files\Adobe\Adobe Photoshop CC 2018\Photoshop.exe')
    for f in os.listdir(copied_path + '\\Hires'):
        subprocess.Popen("%s %s" % (photoshop_path,f))
    os.startfile(copied_path + '\\Hires')
    input('Done?\n Hit enter!')
    moving_files_back()

def moving_files_back():
    os.chdir(os.path.join(os.environ['USERPROFILE'], "Downloads"))
    for refiles in os.listdir(os.path.join(os.environ['USERPROFILE'], "Downloads")):
        if os.path.isfile(refiles):
            shutil.move(refiles, copied_path + '\\1920')
    for folder in os.listdir(copied_path):
        if not os.listdir(copied_path + "\\" + folder):
            send2trash.send2trash(copied_path + "\\" + folder)
    today_date = date.today()
    reversed_date = str(today_date.day) + '-'+ str(today_date.month) + '-' + str(today_date.year)
    os.makedirs(copied_path + '\\' + reversed_date)
    # for file in os.listdir(copied_path)[1:]:
    #     print(os.isdir(file))
    #     shutil.move(file, copied_path + '\\10-10-2018')


# def sending_files_to_ftp():

if __name__ == "__main__":
    start()

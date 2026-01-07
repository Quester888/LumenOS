import os
import sys
import platform
import tkinter as tk

basedir = os.getcwd()

accessdev = ["Windows", "Linux"]
filetointdir = ["L;", "Drivers", "System", "Lumeninate"]
fileforl = ["documents"]
filesforsys = [
    "LumenOsSystem",
    "System16",
    "Usersconfig",
    "bootemp",
    "NBFT",
    "Protocol",
    "FileWriting",
]

decodelog = [
    'encodedalphabet = [',
    '  "J",',
    '  "r",',
    '  "n",',
    '  "b",',
    '  "f",',
    '  "t",',
    '  "c",',
    '  "q",',
    '  "x",',
    '  "m",',
    '  "k",',
    '  "z",',
    '  "L",',
    '  "p",',
    '  "s",',
    '  "y",',
    '  "v",',
    '  "w",',
    '  "a",',
    '  "o",',
    '  "e",',
    '  "g",',
    '  "h",',
    '  "d"',
    ']\n'
    'encodednumbers = [',
    '  7,',
    '  3,',
    '  9,',
    '  1,',
    '  5,',
    '  8,',
    '  0,',
    '  4,',
    '  2,',
    '  6,',
    '  12,',
    '  15,',
    '  11,',
    '  14,',
    '  10,',
    '  13,',
    '  17,',
    '  19,',
    '  16,',
    '  18',
    ']'
]


print(f"BaseDir Set as {basedir}")

root = tk.Tk()
root.title("Install LumenOS")
root.geometry("450x450")
delfile = None


def erad(a):
    global delfile
    # second installer step.
    print(a)
    for widget in root.winfo_children():
        widget.destroy()

    i = 0
    welt = tk.Label(root, text="Deleting files")
    weltper = tk.Label(root, text="0%")
    welt.pack(pady=10)
    weltper.pack(pady=10)
    curdir = os.getcwd()
    weltcur = tk.Label(root, text=curdir)
    weltcur.pack(pady=10)

    fulneed = 0
    if len(delfile) > 0:
        need = 100 / len(delfile)
        while i < len(delfile):
            if os.path.exists(delfile[i]):
                os.remove(delfile[i])
                fulneed += need
                weltper.config(text=f"{fulneed}%")
                root.update()
                i += 1
            else:
                raise RuntimeError("File not located")
    print("Eradication complete!")

    global filetointdir
    global fileforlglobal
    global filesforsys

    os.mkdir("LumenOs")
    os.chdir("LumenOs")

    welt.config(text="Creating Folders")

    curdir = os.getcwd()
    weltcur = tk.Label(root, text=curdir)

    i = 0
    need = 100 / len(filetointdir)
    fulneed = 0
    i = 0
    while i < len(filetointdir):
        os.mkdir(filetointdir[i])
        fulneed += need
        weltper.config(text=f"{fulneed}%")
        root.update()
        i += 1

    print("Main folder creation complete")

    os.chdir("L;")

    curdir = os.getcwd()

    weltcur.config(text="curdir")

    welt.config(text="Populating L drive")

    os.mkdir("documents")
    fulneed = 0
    need = 33.3333333333

    os.chdir("documents")
    curdir = os.getcwd()

    weltcur.config(text=curdir)
    os.mkdir("Images")
    fulneed += need
    weltper.config(text=f"{fulneed}%")
    os.mkdir("Downloads")
    fulneed += need
    weltper.config(text=f"{fulneed}%")
    os.mkdir("Welcome to LumenOS")
    fulneed += need
    weltper.config(text=f"{fulneed}%")

    os.chdir("Welcome to LumenOS")

    curdir = os.getcwd()

    weltcur.config(text=curdir)

    welt.config(text="Populating Folders within L;")

    fulneed = 0
    weltper.config(text=f"{fulneed}%")

    curfile = open("Readme On Access!.txt", "w")
    curfile.write(
        "Hi There! Welcome to LumenOS. We have a full tutorial series within this folder! Have a look"
    )
    print(f"Created {curfile}")
    fulneed += 20
    weltper.config(text=f"{fulneed}%")
    curfile.close

    curfile = open("Create A txt file.txt", "w")
    curfile.write(
        "To create a text file, click the above create button and select '.txt'! "
    )
    print(f"Created {curfile}")
    fulneed += 20
    weltper.config(text=f"{fulneed}%")
    curfile.close

    curfile = open("Create A User.txt", "w")
    curfile.write(
        "To create a user file, click settings as an admin and click 'access' before using the create user function!"
    )
    print(f"Created {curfile}")
    fulneed += 20
    weltper.config(text=f"{fulneed}%")
    curfile.close

    curfile = open("test.enr", "w")
    curfile.write(
        "3809h23-9h-298th2-98th9-8th239th23089h23t983h2t8923ht-8932ht34209th23t9h32923h09h39032ht90823th3490h2309832th893t2h3209t8h328t0h32t0823ht9832ht90328th2390h238ht23"
    )
    print(f"Created {curfile}")
    fulneed += 20
    weltper.config(text=f"{fulneed}%")
    curfile.close

    curfile = open("Create A policy.txt", "w")
    curfile.write(
        "To create a policy file, click settings as an admin and click 'policies' before using the create user function!"
    )
    print(f"Created {curfile}")
    fulneed += 20
    weltper.config(text=f"{fulneed}%")
    curfile.close

    os.chdir("..")
    print(os.getcwd())
    os.chdir("..")
    print(os.getcwd())
    os.chdir("..")
    print(os.getcwd())
    os.chdir("System")
    print(os.getcwd())
    
    welt.config(text="Setting up system")
    global decodelog

    fulneed = 0 
    need = 100 / len(decodelog) 
    weltper.config(text=f"{fulneed}%")
    curfile = open("encrypt87232712409yh19d0h21.py", "w")

    i = 0
    while i < len(decodelog):
        
        curfile.write(
        f"{decodelog[i]}\n"

        )
        fulneed += need
        weltper.config(text=f"{fulneed}%")
        
        i += 1
    print(f"Created {curfile}")
    
    weltper.config(text=f"{fulneed}%")
    curfile.close
    
    


def installs1():
    global delfile
    delfile = []
    for file in os.listdir():
        if file.lower().endswith(".txt"):
            print(file)
            delfile.append(file)
        else:
            print(file, " [SKIPPED DUE TO FILTERING] ")
            continue
    for widget in root.winfo_children():
        widget.destroy()
    welt = tk.Label(
        root,
        text=f"The following files will be eradicated: {delfile} | {len(delfile)} File(s) will be eradicated.",
    )
    welt.pack(pady=10)

    welt2 = tk.Button(
        root, text=f"Install and delete files.", command=lambda: erad(delfile)
    )
    welt2.pack(pady=10)


if platform.system() in accessdev:
    print("Install allowed")
    welt = tk.Label(root, text="Welcome to the LumenOS Installer.")
    welt.pack(pady=10)
    welt2 = tk.Label(
        root,
        text=f"Ensure the installer is in the desired installation folder. This folder must be empty, as all contents will be erased during installation.\n Current location: {basedir}",
    )
    welt2.pack(pady=10)

    welt3 = tk.Button(root, text="Install.", command=installs1)
    welt3.pack(pady=10)

else:
    print("Install disallowed")
    welt = tk.Label(
        root,
        text="Your device is incompatible with LumenOS, THe installer will close shortly.",
    )
    welt.pack(pady=10)

    root.after(3000, root.destroy)  # closes after 3 seconds
